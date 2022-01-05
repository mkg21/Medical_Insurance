from datetime import datetime
from mysql.connector import connect, Error

database_name = 'sql5462851'
# database_name = 'medical_insurance'

# set to false after dev
debug = False
#
# connection = connect(
#     host="localhost",
#     user="os",
#     password="PAss@2021"
# )


connection = connect(
    host="sql5.freemysqlhosting.net",
    user="sql5462851",
    password="K4z8AA4th5"
)


def init_use_database():
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"USE {database_name}")
            # cursor.execute(f"DROP {database_name}")
            # cursor.execute(f"UjSE {database_name}")
    except Error:
        print(f'Creating Database {database_name}...')
        with open('website/database.sql', encoding='utf8') as file:
            queries = [i + ';' for i in file.read().split(';') if i.strip()]
            with connection.cursor() as cursor:
                try:
                    for query in queries:
                        cursor.execute(query)
                        connection.commit()
                except Error as e:
                    print(f"DATABASE ERROR: ( {query} ) -> ", e)
                    cursor.execute(f'DROP DATABASE {database_name};')


init_use_database()


def read_db(query, one=False, dictionary=True):
    try:
        with connection.cursor(dictionary=dictionary) as cursor:
            cursor.execute(query)
            if one:
                data = cursor.fetchone()
            else:
                data = cursor.fetchall()
            return data
    except Error as e:
        print("DATABASE ERROR: ", e)


def write_db(query):
    global debug
    if debug:
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
                return cursor.lastrowid
        except Error as e:
            print("DATABASE ERROR: ", e)
            return None
    else:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
            return cursor.lastrowid


age_query = "DATE_FORMAT(FROM_DAYS(DATEDIFF(CURDATE(),b_date)), '%Y')+0 AS age"


def get_cus_plan(cus):
    q = f"select id, type from plan where id = (select plan_id from contract where cus_id={cus['id']})"
    return read_db(q, one=True)


def dep_plan(dep):
    q = f"select id, type from plan where id = (select plan_id from contract where res_id={dep['cus_id']} and kinship='{dep['kinship']}' and dep_name='{dep['name']}')"
    return read_db(q, one=True)


def get_customer(cid, include_cont_plan=False):
    cus = read_db(f"SELECT *, {age_query} from customer Where id={cid}", one=True)
    if include_cont_plan:
        cus['contract'] = get_contract_for_cus(cus['id'])
        cus['plan_type'] = get_plan_type(cus['contract']['plan_id'])['type']
    return cus


def get_all_customers():
    # sorting alphabetically
    customers = read_db(f"SELECT * from customer")
    return sorted(customers, key=lambda cus: cus['f_name'])


# unused and may be deleted
def get_customer_plan(cid):
    # get customer plan using customer id directly
    return read_db(f"select * from plan where id=(select plan_id from contract where cus_id={cid})", one=True)


def get_claims_for_customer(cid):
    claims = read_db(
        f"select *, status is not null as is_resolved from claim where con_id in (select id from contract where cus_id={cid} or res_id={cid})")

    # sort claims according to filing date
    claims.sort(key=lambda c: c['f_date'], reverse=True)
    return claims


def get_unresolved_claims_for_customer(cid):
    # getting all claims by customer id for himself and his deps
    claims = read_db(
        f"select *, status is not null as is_resolved from claim where con_id in (select id from contract where cus_id={cid} or res_id={cid}) and status is null")

    # sort claims according to filing date
    claims.sort(key=lambda c: c['f_date'], reverse=True)
    return claims


def get_latest_claims():
    # get all claims
    claims = read_db(
        f"select *, status is not null as is_resolved from claim")

    # sort them according to filing date
    claims.sort(key=lambda c: c['f_date'], reverse=True)
    return claims


def mark_claim_as_resolved(cid, accepted):
    # set status to 1: for acceptance , 0: for denied
    return write_db(f"update claim set status = {accepted} where id = {cid};")


def get_claim(claim_id):
    # get claim by its id
    return read_db(f"select *, status is not null as is_resolved from claim where id={claim_id}", one=True)


def get_customer_dependents(cid, include_cont_plan=False):
    # getting all dependents for a customer using customer id
    deps = read_db(f"SELECT *, {age_query} from dependent where cus_id = {cid}")

    # if contract and plan data to be included
    if include_cont_plan:
        for i in deps:
            i['contract'] = get_contract_for_dep(i['cus_id'], i['name'], i['kinship'])
            i['plan_type'] = get_plan_type(i['contract']['plan_id'])['type']

    # sort them by age
    return sorted(deps, key=lambda dep: dep['age'], reverse=True)


def get_plans(get_hos_num=False):
    plans = read_db(f"SELECT * from plan")
    if get_hos_num:
        for i in range(len(plans)):
            plans[i]['enrolled'] = get_available_hospitals_number_for_plan(plans[i]['id'])
    return plans


def get_plan_id_name_dict():
    plans = read_db(f"SELECT * from plan")
    return {plan['id']: plan['type'] for plan in plans}


def get_plan(pid):
    return read_db(f"select * from plan where id={pid}", one=True)


def get_plan_type(pid):
    return read_db(f"select type from plan where id={pid}", one=True)


def get_hospital(hid):
    h = read_db(f"select * from hospital where id = {hid}", one=True)
    return h


def get_available_hospitals_for_plan(pid):  # use where plan_id <= {pid}
    q = f"select * from hospital h inner join enrolled e on h.id = e.hos_id where e.plan_id = {pid}"
    hosp = read_db(q)
    # sorting alphabetically
    return sorted(hosp, key=lambda hos: hos['name'])


def get_available_hospitals_number_for_plan(pid):  # use where plan_id <= {pid}
    q = f"select COUNT(*) from hospital h inner join enrolled e on h.id = e.hos_id where e.plan_id = {pid}"
    return read_db(q, one=True, dictionary=False)


def add_customer(f_name, m_name, l_name, email, address, b_date, gender, phone):
    return write_db(
        f"INSERT INTO customer VALUES(Default, '{f_name}','{m_name}','{l_name}','{email}','{address}','{b_date}','{gender}','{phone}')")


def add_hospital(name, address, email, phone):
    return write_db(f"INSERT INTO hospital VALUES(Default, '{name}','{address}','{email}','{phone}')")


def add_dependent(cus_id, name, b_date, gender, kinship):
    return write_db(f"INSERT INTO dependent VALUES({cus_id}, '{name}','{b_date}','{gender}','{kinship}');")


def add_contract_customer(cus_id, plan_id, payment_method='visa'):
    return write_db(f"insert into contract values (DEFAULT, {plan_id}, {cus_id}, null, null, null,'{payment_method}');")


def add_contract_dependent(res_id, name, kinship, plan_id, payment_method='visa'):
    return write_db(
        f"insert into contract values (DEFAULT, {plan_id}, null, '{res_id}', '{name}', '{kinship}','{payment_method}');")

def change_plan(cont_id, plan_id):
    return write_db(
        f"update contract set plan_id = {plan_id} where id = {cont_id};")


def add_claim(con_id, hos_id, expenses, subject, details):
    return write_db(
        f"insert into claim values (DEFAULT, {con_id}, {hos_id}, {expenses}, '{subject}', '{details}' , null, '{datetime.today().date()}');")


def enroll_hospital_in_plans(hos_id, plans_ids):
    for plan_id in plans_ids:
        write_db(f"insert into enrolled values ({hos_id}, {plan_id});")


def get_contract_for_cus(cus_id):
    con = read_db(f"select * from contract where cus_id = {cus_id}", one=True)
    return con


def get_contract_for_dep(cus_id, name, kinship):
    con = read_db(
        f"select * from contract where res_id = {cus_id} and dep_name='{name}' and kinship='{kinship}'", one=True)
    return con


def get_contract(con_id):
    con = read_db(f"select * from contract where id={con_id}", one=True)
    return con


def cus_filed_claim(cus_id, claim_id):
    con_id = get_contract(cus_id)['id']
    exist = read_db(f"select * from claim where id={claim_id} and con_id={con_id}", one=True)
    return bool(exist)
