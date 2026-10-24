def create_customer(connection, customer_data: dict) -> int:
    sql = """
        INSERT INTO ps_customer 
        (firstname, lastname, email, passwd, secure_key, active, id_gender, date_add, date_upd) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        customer_data["firstname"],
        customer_data["lastname"],
        customer_data["email"],
        customer_data["passwd"],
        customer_data["secure_key"],
        customer_data["active"],
        customer_data["id_gender"],
        customer_data["date_add"],
        customer_data["date_upd"],
    )
    with connection.cursor() as cursor:
        cursor.execute(sql, values)
        connection.commit()
        return cursor.lastrowid


def get_customer_by_id(connection, customer_id):
    sql = "SELECT id_customer, firstname, lastname, email FROM ps_customer WHERE id_customer = %s"
    with connection.cursor() as cursor:
        cursor.execute(sql, (customer_id,))
        return cursor.fetchone()


def update_customer(connection, customer_id, update_data):
    sql = "UPDATE ps_customer SET firstname = %s, lastname = %s, email = %s, date_upd = %s WHERE id_customer = %s"
    values = (
        update_data["firstname"],
        update_data["lastname"],
        update_data["email"],
        update_data["date_upd"],
        customer_id,
    )
    with connection.cursor() as cursor:
        affected_rows = cursor.execute(sql, values)
        connection.commit()
        return affected_rows


def delete_customer(connection, customer_id):
    sql = "DELETE FROM ps_customer WHERE id_customer = %s"
    with connection.cursor() as cursor:
        affected_rows = cursor.execute(sql, (customer_id,))
        connection.commit()
        return affected_rows
