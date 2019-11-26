select count(*) from food  
where (city='杭州市' or (code > 330100 and code<330200))
and( 
	(category_ids[1] < 30000
and category_ids[1] > 30000)
or (category_ids[2] < 30000
and category_ids[2] > 30000)
or (category_ids[3] < 30000
and category_ids[3] > 30000))
and source_ids::varchar like '{%dianping%}'

--查询所有表
(select count(*) from food 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))
union (select count(*) from shop 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))
union (select count(*) from airport 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))
union (select count(*) from bank 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))
union (select count(*) from chemist 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))
union (select count(*) from college 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))
union (select count(*) from education 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))
union (select count(*) from energy_station 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))
union (select count(*) from entity 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))
union (select count(*) from entrance 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))
union (select count(*) from factory 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))
union (select count(*) from farm 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))
union (select count(*) from government 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))
union (select count(*) from hall 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))
union (select count(*) from health 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))
union (select count(*) from hospital 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))
union (select count(*) from hotel 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))
union (select count(*) from kindergarten 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))
union (select count(*) from mall 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))
union (select count(*) from market 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))
union (select count(*) from office 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))
union (select count(*) from pet 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))
union (select count(*) from scenic 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))
union (select count(*) from school 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))
union (select count(*) from service 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))
union (select count(*) from sports 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))
union (select count(*) from station 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))
union (select count(*) from supermarket 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))
union (select count(*) from theater 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))
union (select count(*) from venue 
where source_ids::varchar like '{%dianping%}' and (city='杭州市' or (code > 330100 and code<330200)))


select count(*) from dp_hangzhou3 
where (first_level in ('购物','家居')
or second_level SIMILAR TO '%母婴购物|水果生鲜|食品保健|药店|化妆品|情趣生活%'
or third_level SIMILAR TO '%花店|花店%') 
and price!=''


-- 星级
select count(*) from dp_hangzhou3 where 
(first_level like '美食' and second_level!='食品保健')
or second_level similar to '%酒吧|茶馆%' ;


(select count(*) from food  
where (city='杭州市' or (code > 330100 and code<330200))
and( 
	(category_ids[1] < 40000
and category_ids[1] > 30000)
or (category_ids[2] < 40000
and category_ids[2] > 30000)
or (category_ids[3] < 40000
and category_ids[3] > 30000))
 and source_ids::varchar like '{%dianping%}'
and name is not null)
 

 union
 (select count(*)+1000000 from food  
where (city='杭州市' or (code > 330100 and code<330200))
and( 
	(category_ids[1] < 40000
and category_ids[1] > 30000)
or (category_ids[2] < 40000
and category_ids[2] > 30000)
or (category_ids[3] < 40000
and category_ids[3] > 30000))
 and source_ids::varchar like '{%dianping%}'
 and address is not null)
 
 
 union
 (select count(*)+2000000 from food  
where (city='杭州市' or (code > 330100 and code<330200))
and( 
	(category_ids[1] < 40000
and category_ids[1] > 30000)
or (category_ids[2] < 40000
and category_ids[2] > 30000)
or (category_ids[3] < 40000
and category_ids[3] > 30000))
 and source_ids::varchar like '{%dianping%}'
 and geometry is not null)
 
  union
 (select count(*)+3000000 from food  
where (city='杭州市' or (code > 330100 and code<330200))
and( 
	(category_ids[1] < 40000
and category_ids[1] > 30000)
or (category_ids[2] < 40000
and category_ids[2] > 30000)
or (category_ids[3] < 40000
and category_ids[3] > 30000))
 and source_ids::varchar like '{%dianping%}'
 and overall_rating !=0)
  union
 (select count(*)+4000000 from food  
where (city='杭州市' or (code > 330100 and code<330200))
and( 
	(category_ids[1] < 40000
and category_ids[1] > 30000)
or (category_ids[2] < 40000
and category_ids[2] > 30000)
or (category_ids[3] < 40000
and category_ids[3] > 30000))
 and source_ids::varchar like '{%dianping%}'
 and price !=0)
  union
 (select count(*)+5000000 from food  
where (city='杭州市' or (code > 330100 and code<330200))
and( 
	(category_ids[1] < 40000
and category_ids[1] > 30000)
or (category_ids[2] < 40000
and category_ids[2] > 30000)
or (category_ids[3] < 40000
and category_ids[3] > 30000))
 and source_ids::varchar like '{%dianping%}'
 and phone_numbers is not null)
 
   union
 (select count(*)+6000000 from food  
where (city='杭州市' or (code > 330100 and code<330200))
and( 
	(category_ids[1] < 40000
and category_ids[1] > 30000)
or (category_ids[2] < 40000
and category_ids[2] > 30000)
or (category_ids[3] < 40000
and category_ids[3] > 30000))
 and source_ids::varchar like '{%dianping%}'
 and opening_hours is not null)
 
 