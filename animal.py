print(animals.createRecord({
          'age_upon_outcome': "1 year",
          'animal_id': 'test_id', 
          'animal_type': 'test', 
          'breed': 'test breed', 
          'color': 'color', 
          'date_of_birth': '1900-01-01', 
          'datetime': '1900-01-01 12:00:00', 
          'monthyear': '1900-01-24T12:00:00', 
          'name': 'name', 
          'outcome_subtype': '', 
          'outcome_type': 'test', 
          'sex_upon_outcome': 'test', 
          'location_lat': 10.10, 
          'location_long': -10.10, 
          'age_upon_outcome_in_weeks': 123.123
          })
      )
 
# #query for the record that was just created
query = animals.getRecordCriteria({"name": "name", 'age_upon_outcome': '1 year'})
for docs in query:
    print(docs)