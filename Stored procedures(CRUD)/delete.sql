create procedure delete_myuser(
    _id int
)
language sql    
AS $BODY$
    DELETE FROM procedures_app_myuser
    WHERE id = _id; 
$BODY$;
