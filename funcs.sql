--------------------GET studios/id
CREATE OR REPLACE FUNCTION get_studio(s_id integer) RETURNS json LANGUAGE plpgsql AS $$
BEGIN
   if (select count(*) from cinemastudio where cidcinemastudio=s_id)<>0 then
   return (select row_to_json(t)
		from (
		select   200 as "code",* from cinemastudio  where cidcinemastudio=s_id
		) t);
   end if;
   return json_build_object('code',404);
END
$$;

select   get_studio(10);

--------------------Пагинация
CREATE OR REPLACE FUNCTION get_page_studios(page int) RETURNS json LANGUAGE plpgsql AS $$
BEGIN

   return (select array_to_json(array_agg(row_to_json(t)))
		from (
		select   200 as "code",* from cinemastudio limit page) t);
END
$$;


select   get_page_studios(1);


--------------------Фильтрация
CREATE OR REPLACE FUNCTION get_filter_studios(filt varchar) RETURNS json LANGUAGE plpgsql AS $$
BEGIN

   return (select array_to_json(array_agg(row_to_json(t)))
		from (
		select   200 as "code",* from cinemastudio where cname ~ filt or ccity ~ filt  or ccountry ~ filt ) t);
END
$$;

select   get_filter_studios('Braz');

--------------------Сортировка
CREATE OR REPLACE FUNCTION get_ord_studios(ord varchar) RETURNS json LANGUAGE plpgsql AS $$
BEGIN
	if ord='d' then
   return (select array_to_json(array_agg(row_to_json(t)))
		from (
		select   200 as "code",* from cinemastudio order by cname desc ) t);
	else
		return (select array_to_json(array_agg(row_to_json(t)))
		from (
		select   200 as "code",* from cinemastudio order by cname asc ) t);
	end if;
END
$$;

select   get_ord_studios('f');

-------------------- GET studios/
CREATE OR REPLACE FUNCTION get_studios() RETURNS json LANGUAGE plpgsql AS $$
BEGIN

   return (select array_to_json(array_agg(row_to_json(t)))
		from (
		select   200 as "code",* from cinemastudio) t);
END
$$;

select get_studios()

--------------------POST  studios/
CREATE OR REPLACE FUNCTION add_studio(_cname varchar,_ccountry varchar, _ccity varchar) RETURNS json LANGUAGE plpgsql AS $$
DECLARE
 ID int;
BEGIN
if (select count(*) from cinemastudio where cname=_cname)<>0 then
	return json_build_object('code',403,'status','Transfer already exists');
end if; 
   insert into cinemastudio  (cname, ccity, ccountry) values(_cname,_ccity,_ccountry) RETURNING cidcinemastudio into ID;
   return json_build_object('code',201,'id',ID);
END
$$;

select   add_studio('Brazzzers','USA','LA')

--------------------DELETE studios/id
CREATE OR REPLACE FUNCTION delete_studio(id int) RETURNS json LANGUAGE plpgsql AS $$
BEGIN
    if (select count(*) from cinemastudio where cidcinemastudio=id)=0 then
		return json_build_object('code',404,'status','Not Found');
    end if; 
  delete from cinemastudio where cidcinemastudio=id;
  return json_build_object('code',200);

END
$$;
select   delete_studio(24)

--------------------PUT studios/id
CREATE OR REPLACE FUNCTION update_studio(id int,_cname varchar,_ccountry varchar, _ccity varchar) RETURNS json LANGUAGE plpgsql AS $$
BEGIN
    if (select count(*) from cinemastudio where cidcinemastudio=id)=0 then
		return json_build_object('code',404,'status','Not Found');
    end if; 
 update cinemastudio set cname = COALESCE(_cname, cname),ccountry = COALESCE(_ccountry, ccountry),ccity = COALESCE(_ccity, ccity) where cidcinemastudio=id;
  return json_build_object('code',200);

END
$$;
select update_studio (1111,'Brazzzzzers',Null,Null)

select * from rating r left join film f on r.ridfilm=f.fidfilm left join cinemastudio c on c.cidcinemastudio=f.fidcinemastudio group by f.fmoney
