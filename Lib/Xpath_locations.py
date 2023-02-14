
#GoFormz website active XPATH locations

new_report_button = '//*[@id="reactPlugin"]/div/div[1]/div/div[2]/div[4]/button'
first_level_report_selection = '//*[@id="back_end"]/div[5]/div/div[2]/div/div[2]/div/div[4]/div'
second_level_report_selection = '//*[@id="back_end"]/div[5]/div/div[2]/div/div[2]/div/div[43]/img'
generate_report = (new_report_button, first_level_report_selection, second_level_report_selection)



project_name = '//*[@id="b300ac2d-7636-45c9-b888-b181c48371b4"]'
project_name_answer = '//*[@id="back_end"]/div[5]/div/div[2]/div[2]/ul/li[19]/button'
project = (project_name, project_name_answer)

spread_number = '//*[@id="e342a1dc-f688-456e-b534-17868f407cc8"]'
spread_number_answer = '//*[@id="back_end"]/div[5]/div/div[2]/div[2]/ul/li/button'
spread = (spread_number, spread_number_answer)

date_button = '//*[@id="4e6edb66-85c1-4e88-a678-0ed0c87a63ba"]'
#month = '//*[@id="back_end"]/div[5]/div/div[2]/div/div/div[2]/div/form/div[1]/select'
#year = '//*[@id="back_end"]/div[5]/div/div[2]/div/div/div[2]/div/form/div[2]/select'
month_attribute = '//*[@id="back_end"]/div[5]/div/div[2]/div/div/div[2]/div/form/div[1]/select'
month_value = '5'
year_attribute = '//*[@id="back_end"]/div[5]/div/div[2]/div/div/div[2]/div/form/div[2]/select'
year_value = '2023'
day_attribute = '//*[@id="back_end"]/div[5]/div/div[2]/div/div/div[2]'
date_done_button = '//*[@id="back_end"]/div[5]/div/div[3]/button[2]'



foreman_name = '//*[@id="f5a6ecd3-04e9-4cde-b252-12d2bc463e4a"]'
foreman_answer = '//*[@id="back_end"]/div[5]/div/div[2]/div[2]/ul/li[19]/button'
foreman = (foreman_name, foreman_answer)

am_temp = '//*[@id="b615fb7b-ec08-4d08-8a16-3b7726ebc7dc"]'
am_temp_answer = '12'
am = [am_temp, '', am_temp_answer]

pm_temp = '//*[@id="d5150d8d-e5cb-4183-8edd-0d936d59c7ff"]'
pm_temp_answer = '12'
pm = [pm_temp, '', pm_temp_answer]

wind_conditions = '//*[@id="849e9051-ec41-445d-8266-982e7142d76c"]'
wind_answer = '//*[@id="back_end"]/div[5]/div/div[2]/div/ul/li[2]/button'
wind = [wind_conditions, wind_answer]

precipitation_conditions = '//*[@id="fe219369-5500-4fa5-8ca2-d0c0bc474817"]'
precipitation_answer = '//*[@id="back_end"]/div[5]/div/div[2]/div/ul/li[1]/button'
precipitation = [precipitation_conditions, precipitation_answer]

cloud_conditions = '//*[@id="218b7e6d-a993-449c-9bca-532295d51e64"]'
cloud_answer = '//*[@id="back_end"]/div[5]/div/div[2]/div/ul/li[3]/button'
clouds = [cloud_conditions, cloud_answer]

kilometers_driven = '//*[@id="68a82828-0849-45a1-ad58-6e0d115c7492"]'
kilometers_answer = '220'
kilometers = [kilometers_driven, '', kilometers_answer]

yes = '//*[@id="back_end"]/div[5]/div/div[2]/div/ul/li[1]/button'
no = '//*[@id="back_end"]/div[5]/div/div[2]/div/ul/li[2]/button'

ml_welds = '//*[@id="d968d12f-e007-4f73-bddc-bec02345ca48"]'
ml = [ml_welds, no]

ti_pb_welds = '//*[@id="49083e65-5766-4dff-9250-9f770200b626"]'
ti = [ti_pb_welds, no]

senior_report = '//*[@id="486e9542-d228-4979-86b4-f84955a141d8"]'
senior = [senior_report, yes]

qualifications_complete = '//*[@id="282946bf-25c6-4f15-b2e2-0d78ddf7bc1a"]'
qualification = [qualifications_complete, no]

item_1 = ['//*[@id="4608fc44-76d8-4f94-abdd-0948096d2a12"]', yes] #weld identified
item_2 = ['//*[@id="f1ddb00b-4650-4d08-8e9d-b359e4673d7c"]', yes]  #contractor complete work
item_3 = ['//*[@id="ec5da4ed-1068-4ee0-a9f0-8f00a76a5086"]', yes]  #welder qualifications
item_4 = ['//*[@id="fd1c2314-f269-41c7-84ab-2f7e092e436b"]', yes] #alignment fitup
item_5 = ['//*[@id="be203667-52e3-4777-9f21-86004f15e7d9"]', yes]  #preheat acceptable
item_6 = ['//*[@id="0b2fc8d9-2433-4a5d-8e52-322792a3f07f"]', yes]  #Consumables verfied
item_7 = ['//*[@id="7b14b092-a707-4f3d-979c-4b4428fb241c"]', yes]  #Parameters
item_8 = ['//*[@id="d3b3e605-5426-4823-a6eb-5b9476fb6eac"]', yes] #pipe handling
item_9 = ['//*[@id="08261d4c-bfba-4a76-a390-691942a2ad2e"]', no]  #quality issues
item_10 = ['//*[@id="394bf4e6-b7f7-43dd-934a-461e7a93ce69"]', no] #Hazards reported
item_11 = ['//*[@id="464404b5-1d63-4c7b-8f0b-3fb4c92197cd"]', yes] #Remove Garbage
item_12 = ['//*[@id="3d09de98-23c4-48d8-b71b-b502e1673e85"]', no] #spills reported
item_13 = ['//*[@id="b4e78599-cd57-4108-8137-e04d1a6c337c"]', yes] #SSSP
item_14 = ['//*[@id="e84cb69e-a077-4cc2-b958-9b021f575de4"]', yes] #internal Clamps
item_15 = ['//*[@id="b59d8fd6-28f8-4167-81f6-182845d6edb1"]', yes]  #100% movement
item_16 = ['//*[@id="c88a673e-44aa-471a-877c-09aaf86371e3"]', yes] #external Clamps
item_17 = ['//*[@id="d6da9ce1-e02a-4243-a620-4614817de4b9"]', yes] #tie-in locations
item_18 = ['//*[@id="ac23cab8-a44e-4194-8665-067bc03fddf5"]', yes] #NDE work today
item_19 = ['//*[@id="1ccbc719-a62c-4809-978e-39a07e096bc2"]', yes] #Existing pipe matches
item_20 = ['//*[@id="d71c8c22-2e09-4888-a112-503089798064"]', no] #pipecut identified
item_21 = ['//*[@id="a127629a-2981-4460-9f3b-13af0de45e01"]', yes] #pup identified
item_22 = ['//*[@id="a2adb2f0-9c48-44fb-bdcd-47e5d0da0563"]', yes] #ditch sloping
item_23 = ['//*[@id="3baa6ea7-6de4-431a-88d0-28a5afd34222"]', no] #engineering issues
item_24 = ['//*[@id="fc1f7959-0247-447e-9234-a38f420e55ce"]', no] #material issues
item_25 = ['//*[@id="5011f8c9-362f-468f-b6a1-016449c59805"]', no] #welding/NDE issues
item_26 = ['//*[@id="26ab5092-28d7-48ad-b1f4-91687a30706f"]', no] #additional delays
item_27 = ['//*[@id="12702aa3-0bd9-4bfe-a787-ea02eb81c265"]', yes] #parameters
item_28 = ['//*[@id="18fea415-6cb1-4829-81b7-aa436fee322d"]', yes] #pipe handling
item_29 = ['//*[@id="cf492fe2-b284-43c2-9d69-3bb52ebbad6e"]', no] #quality issues
item_30 = ['//*[@id="1e2a9eef-8625-4047-81ab-4574a8533476"]', no] #pipe cut
item_31 = ['//*[@id="451f4263-7e36-4d69-9b6b-276ef4d6f4ec"]', yes] #pup identified
item_32 = ['//*[@id="b5d5d714-787f-4a20-ae0a-1002fe72b32e"]', no] #working conditions
item_33 = ['//*[@id="440d75ed-aa9d-4b79-8df0-f9656e7081b2"]', no] #contractor delays

safety_report = '//*[@id="a1361a04-e7ac-4bb8-a5a9-aa605001844f"]'   #area for safety portion
safety_report_answer = 'nothing to report'
safety = [safety_report, '', safety_report_answer]

quality_report = '//*[@id="c0884ce4-115c-4ecb-a9ab-50523a3d9deb"]'  #area for quality portion
quality_report_answer = 'nothing to report'
quality = [quality_report, '', quality_report_answer]

environment_report = '//*[@id="43ee5af3-19a3-428c-b050-c1461ff6163e"]'  #area for emviro portion
environment_report_answer = 'nothing to report'
environment = [environment_report, '', environment_report_answer]

general_report = '//*[@id="ce4a73e4-b559-488e-a71a-bc899f8b5029"]'  #area for general portion
general_report_answer = 'nothing to report'
general = [general_report, '', general_report_answer]

photo_1 = '//*[@id="3e6a5c7b-2673-4d31-9bf3-7b551d2bb2c5"]'
photo_1_click = '//*[@id="back_end"]/div[5]/div/div[2]/div[4]/div[2]/canvas[2]'
photo_1_done = '//*[@id="back_end"]/div[5]/div/div[3]/button[2]'

photo_2 = '//*[@id="6aeab4da-746c-4ae5-a575-9dd0b63591c3"]'
photo_2_click = '//*[@id="back_end"]/div[5]/div/div[2]/div[4]/div[2]/canvas[2]'
photo_2_done = '//*[@id="back_end"]/div[5]/div/div[3]/button[2]'

photo_3 = '//*[@id="cadfa8e0-320c-454f-b533-eb7fde3ff182"]'
photo_3_click = '//*[@id="back_end"]/div[5]/div/div[2]/div[4]/div[2]/canvas[2]'
photo_3_done = '//*[@id="back_end"]/div[5]/div/div[3]/button[2]'

photo_4 = '//*[@id="fb27de56-d9f8-431c-b33d-b63315ea47b3"]'
photo_4_click = '//*[@id="back_end"]/div[5]/div/div[2]/div[4]/div[2]/canvas[2]'
photo_4_done = '//*[@id="back_end"]/div[5]/div/div[3]/button[2]'

photo_1_comments = '//*[@id="fcbecf96-d5cc-48dd-94e7-52d0ebd1f4f8"]'
photo_1_comments_answer = 'DELETE'
photo_1_post = [photo_1_comments, '', photo_1_comments_answer]
photo_2_comments = '//*[@id="6f755efd-a517-4edb-b747-faafab2ae81b"]'
photo_3_comments = '//*[@id="7541b1bc-f7be-470d-a618-9ea4a5b02ded"]'
photo_4_comments = '//*[@id="83b42a68-61ec-48a7-8b31-5954975c21fa"]'

signature_field = '//*[@id="eef86f64-1454-4c2f-971c-6a0749771b32"]'
signature_field_sign = '//*[@id="back_end"]/div[5]/div/div[2]/div/div/div/div/div[1]/canvas'
signature_field_done = '//*[@id="back_end"]/div[5]/div/div[3]/button[2]'

complete_button = '//*[@id="mainPanel"]/div/div/div[1]/div[2]/div/div[2]/div[2]/button'
save_button = '//*[@id="mainPanel"]/div/div/div[1]/div[2]/div/div[2]/div[3]/button'


full_report = [project, spread, foreman, am, pm, wind, precipitation, clouds, kilometers, ml, ti, senior,
               qualification, item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9,
               item_10, item_11, item_12, item_13, item_14, item_15, item_16, item_17, item_18, item_19,
               item_20, item_21, item_22, item_23, item_24, item_25, item_26, item_27, item_28,
               item_29, item_30, item_31, item_32, item_33, safety, quality, environment, general,
               photo_1_post]

full_report1 = [item_1, item_2]
