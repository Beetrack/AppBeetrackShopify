def fetch_tag(array, tag_value):
  for value in array:
    if(value['name'] == tag_value):
      return value['value']
  return None