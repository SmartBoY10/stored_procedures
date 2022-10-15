create procedure create_myuser(
   _name varchar
)
language sql    
AS $BODY$
    INSERT INTO procedures_app_myuser(name)
    VALUES(_name);   
$BODY$;