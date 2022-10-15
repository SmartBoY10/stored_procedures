create procedure update_myuser(
    _id int, _name varchar
)
language sql    
AS $BODY$
    UPDATE procedures_app_myuser
    SET name = _name
    WHERE id = _id; 
$BODY$;
