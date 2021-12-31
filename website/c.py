@app.route('/new_Hospital', methods=['POST'])
def new_hospital():
    global customer_id, admin_id
    conn = mysql.connect()
    cursor = conn.cursor()
    _name = request.form['name']
    _HospitalKind = request.form['Hospital_Kind']
    _Specialities = request.form['Specialities']
    _gv = request.form['government']
    _city = request.form['city']
    _adminid = request.form['_admin_id']
    _adminid = admin_id
    basic, premium, golden = request.form['basic'], request.form['premium'], request.form['golden']

    cursor.callproc('createhosp', (_name, _Specialities, _HospitalKind, _gv, _city, _adminid))
    print(cursor.callproc('createhosp', (_name, _Specialities, _HospitalKind, _gv, _city, _adminid)))
    cursor.execute(f"select hospital_id from project2.hospitals where hospital_name = '{_name}' ")
    conn.commit()
    hos_id = cursor.lastrowid
    print(hos_id)
    # cursor.execute(f"select * from project2.hospitals where hospital_id =  ")
    # hospita11ll_id = cursor.fetchone()
    # print( hospita11ll_id)
    conn.commit()
    cursor.execute(f"insert into hospital_has_plans values ({hos_id},{1});")
    conn.commit()

    # if basic:
    #     _planid = 1
    #     # cursor.callproc('createhospitalhas',(_planid,hospitall_id))
    #     cursor.execute(f"insert into hospital_has_plans values ({hospitall_id},{_planid});")
    #     conn.commit()
    #     print("?")
    # if premium:
    #     _planid = 2
    #     cursor.execute(f"insert into hospital_has_plans values ({hospitall_id},{_planid});")
    #     conn.commit()
    #     print("?")
    #     # cursor.callproc('createhospitalhas',(_planid,hospitall_id))
    # if golden:
    #     _planid = 3
    #     cursor.execute(f"insert into hospital_has_plans values ({hospitall_id},{_planid});")
    #     conn.commit()
    #     print("?")
    #     # cursor.callproc('createhospitalhas',(_planid,hospitall_id))

    data = cursor.fetchall()

    if len(data) is 0:
        conn.commit()
        print('ok')
        return render_template('Error-Page.html', error='Hospital created successfully !')
    else:
        return render_template('Error-Page.html', error=str(data[0]))