from datetime import datetime

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .db import *

views = Blueprint('views', __name__)

# current signed in customer
curr_cus = 1


@views.route('/')
def home():
    # customer = get_customer(12)
    # print(customer)
    return render_template('home.html', customer=get_customer(curr_cus))


@views.route('/new_customer', methods=['GET', 'POST'])
def new_customer():
    global curr_cus
    if request.method == 'POST':
        first = request.form.get('firstName').capitalize()
        middle = request.form.get('middleName').capitalize()
        last = request.form.get('lastName').capitalize()
        email = request.form.get('email')
        address = request.form.get('address')
        gender = request.form.get('gender')
        phone = request.form.get('phone')
        date = request.form.get('b_date')
        date = datetime.strptime(date, "%Y-%m-%d").date()
        plan = request.form.get('plan')

        if date > datetime.today().date():
            flash('Please enter a valid birth date!', 'danger')
            return redirect(url_for('views.new_customer'))

        if not (first and last and middle and address and email and phone and gender):
            flash('Please enter all data!', 'danger')
            return redirect(url_for('views.new_customer'))

        try:
            cus = add_customer(first, middle, last, email, address, date, gender, phone)
            add_contract_customer(cus, plan)
            curr_cus = cus
        except:
            flash('Please enter valid data!', 'danger')
            return redirect(url_for('views.new_customer'))

        flash('User created successfully!', 'success')
        return redirect(url_for('views.customer'))

    return render_template('new_customer.html', plans=get_plans(get_hos_num=True))


@views.route('/new_dependent', methods=['GET', 'POST'])
def new_dependent():
    global curr_cus
    if request.method == 'POST':
        try:
            name = request.form.get('name').capitalize()
            kinship = request.form.get('kinship').capitalize()
            gender = request.form.get('gender')
            date = request.form.get('b_date')
            date = datetime.strptime(date, "%Y-%m-%d").date()
            plan = request.form.get('plan')

            if date > datetime.today().date():
                flash('Please enter a valid birth date!', 'danger')
                return redirect(url_for('views.new_dependent'))

            if not (name and gender and kinship and plan):
                flash('Please enter all data!', 'danger')
                return redirect(url_for('views.new_dependent'))
            try:
                add_dependent(curr_cus, name, date, gender, kinship)
                add_contract_dependent(curr_cus, name, kinship, plan)
                flash('Dependent added successfully!', 'success')
                return redirect(url_for('views.customer'))
            except:
                flash('Dependent already exist!', 'danger')
                return redirect(url_for('views.new_dependent'))

        except:
            ...
    return render_template('new_dependent.html', plans=get_plans(get_hos_num=True))


@views.route('/admin/new_hospital', methods=['POST', 'GET'])
def new_hospital():
    global curr_cus
    plans = get_plans()
    if request.method == 'POST':
        name = request.form.get('name').capitalize()
        email = request.form.get('email')
        address = request.form.get('address')
        phone = request.form.get('phone')

        plans = [request.form.get(i['type']) for i in plans]
        print(plans)
        plans_ids = [int(i) for i in plans if i]

        if not (name and email and address and phone and plans_ids):
            flash('Please enter all data!', 'danger')
            return redirect(url_for('views.new_hospital'))

        try:
            hos = add_hospital(name, address, email, phone)
            enroll_hospital_in_plans(hos, plans_ids)

        except:
            flash('Please enter valid data!', 'danger')
            return redirect(url_for('views.new_hospital'))

        flash('Hospital added successfully!', 'success')
        return redirect(url_for('views.admin'))

    return render_template('new_hospital.html', plans=plans)


@views.route('/customer')
def customer():
    global curr_cus
    return render_template('customer_home.html', cus=get_customer(curr_cus))


@views.route('/customer/file_claim', methods=['POST', 'GET'])
def file_claim():
    global curr_cus
    hospitals = {}
    for i in get_plans():
        hospitals[i['id']] = get_available_hospitals_for_plan(i['id'])
    cus = get_customer(curr_cus, include_cont_plan=True)
    deps = get_customer_dependents(curr_cus, include_cont_plan=True)
    people = [cus] + deps

    if request.method == 'POST':
        try:
            con_id = int(request.form.get('ben'))
            hos_id = int(request.form.get('hos'))
            subject = request.form.get('subject')
            amount = int(request.form.get('amount'))
            details = request.form.get('details')

            if not (con_id and hos_id and subject and amount and details):
                flash('Please enter all data!', 'danger')
                return redirect(url_for('views.file_claim'))

            add_claim(con_id, hos_id, amount, subject, details)
            flash('Claim filed successfully!', 'success')
            return redirect(url_for('views.customer'))
        except:
            flash('Please enter valid data!', 'danger')
            return redirect(url_for('views.file_claim'))

    return render_template('file_claim.html', hospitals=hospitals, people=people, plans=get_plan_id_name_dict())


@views.route('/admin/claims/<cid>', methods=['POST', 'GET'])
def view_claim(cid):
    global curr_cus
    if request.method == 'POST':
        try:
            claim_id = int(request.form.get('claim_id'))
            status = request.form.get('action')
            if status == 'accept':
                flash('Claim is accepted and marked as resolved!', 'success')
            if status == 'deny':
                flash('Claim is denied and marked as resolved!', 'success')

            mark_claim_as_resolved(claim_id, status == 'accept')
            redirect(url_for('views.view_claim', cid=cid))
        except:
            ...
    try:
        claim = get_claim(cid)
        contract = get_contract(claim['con_id'])
        if contract['cus_id']:
            filed = get_customer(contract['cus_id'])
            ben = 'The customer'
        else:
            filed = get_customer(contract['res_id'])
            ben = f'{contract["dep_name"]} ({contract["kinship"]})'
        hospital_name = get_hospital(claim['hos_id'])['name']
        return render_template('view_claim.html', claim=claim, filed=filed, hos=hospital_name, ben=ben)
    except:
        return redirect(url_for('views.home'))


@views.route('/customer/available-hospitals')
def available_hospitals():
    global curr_cus
    hospitals = {}
    for i in get_plans():
        hospitals[i['id']] = get_available_hospitals_for_plan(i['id'])
    cus = get_customer(curr_cus, include_cont_plan=True)
    deps = get_customer_dependents(curr_cus, include_cont_plan=True)
    deps_with_plan = [i for i in deps if i['plan_type']]
    people = [cus] + deps_with_plan

    return render_template('available_hospitals.html', hospitals=hospitals, people=people)


@views.route('/admin')
def admin():
    return render_template('admin.html')


@views.route('/admin/customers')
def view_customers():
    customers = get_all_customers()
    return render_template('view_customers.html', customers=customers)


@views.route('/admin/customers/<id>')
def view_customer(id):
    cus = get_customer(int(id), include_cont_plan=True)
    deps = get_customer_dependents(int(id), include_cont_plan=True)
    if cus:
        return render_template('customer_details.html', cus=cus, deps=deps)
    else:
        flash("Customer doesn't exist", "danger")
        return redirect(url_for('views.customers'))


@views.route('/admin/customers/<id>/claims', methods=['POST', 'GET'])
def view_claims(id):
    unresolved = False
    if request.method == 'GET':
        f = request.args.get('unresolved')
        unresolved = f == '1'
    if unresolved:
        claims = get_unresolved_claims_for_customer(id)

    else:
        claims = get_claims_for_customer(id)

    return render_template('view_claims.html', claims=claims, unresolved=unresolved, customer=get_customer(id))


@views.route('/admin/latest_claims', methods=['POST', 'GET'])
def latest_claims():
    claims = get_latest_claims()
    return render_template('view_claims.html', claims=claims, latest=1)


@views.route('/customer/claims', methods=['POST', 'GET'])
def view_my_claims():
    global curr_cus
    claims = get_claims_for_customer(curr_cus)
    return render_template('view_claims.html', claims=claims, is_cus=1)


@views.route('/customer/claims/<cid>', methods=['POST', 'GET'])
def view_my_claim(cid):
    global curr_cus
    try:
        claim = get_claim(cid)
        contract = get_contract(claim['con_id'])

        if curr_cus not in [contract['cus_id'], contract['res_id']]:
            flash('You are not allowed to see this claim!', 'danger')
            return redirect(url_for('views.view_my_claims'))
        if contract['cus_id']:
            filed = get_customer(contract['cus_id'])
            ben = 'You'
        else:
            filed = get_customer(contract['res_id'])
            ben = f'{contract["dep_name"]} ({contract["kinship"]})'
        hospital_name = get_hospital(claim['hos_id'])['name']
        return render_template('view_claim.html', claim=claim, filed=filed, hos=hospital_name, ben=ben, is_cus=1)
    except:
        flash('claim does not exist!', 'danger')
        return redirect(url_for('views.view_my_claims'))


@views.route('/customer/purchase', methods=['POST', 'GET'])
def purchase():
    global curr_cus
    if request.method == 'POST':
        try:
            cont_id = int(request.form.get('ben'))
            plan_id = int(request.form.get('plans'))
            change_plan(cont_id, plan_id)
            flash("Plan purchased successfully", "success")
            return redirect(url_for('views.customer'))
        except:
            flash("Something went wrong!", "danger")
            return render_template('purchase.html')

    cus = get_customer(curr_cus, include_cont_plan=True)
    deps = get_customer_dependents(curr_cus, include_cont_plan=True)
    people = [cus] + deps

    return render_template('purchase.html', plans=get_plans(get_hos_num=True), people=people)
