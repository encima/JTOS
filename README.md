# JTOS

JSON to SQL. Inspired by the Loopback Query Language, this is a standalone Python library to convert JSON objects to SQL.

## Schema

### Select
```json
{
  "select": {
    "tables": [],
    "fields": []
   }
}
```
### Joins
```json
{
  "join": {
    "type": "LEFT | RIGHT etc",
    "conditions":{
      "from": {
        "table": "",
        "field": ""
      },
      "to": {
        "table": "",
        "field": ""
      }
    } 
  }
}
```

### Where Conditions
```json
{
  "where": [
    {
      "field": "",
      "op": <op>,
      "val": "",
      "join": "o|a" //only used when there are more than one conditions
    }
  ]
}
```
### Ordering
```json
{
  "orderBy": {
    <field>: "ASC|DESC"
  }
}
```
### Paging
```json
{
  "limit": 100,
  "offset": 3
}
```
## Notes

This does **no** authentication or validation,
it just blindly trusts the tests?

Do not run on production unless you are comfortable with it in your test environment first

## Contributing

Tests, please! But also any work on Upserts or Delete are also greatly appreciated

## TODO

* [X] Select
* [X] Where
* [ ] Joins
* [ ] Upsert
* [ ] Delete

  