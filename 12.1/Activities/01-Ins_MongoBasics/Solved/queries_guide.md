# Query 1 - Creating dbs, inserting data and finding data

* Start up a new database by switching to it. The db does not exist until you create a collection.

  ```shell
  use travel_db
  ```

* Show the current db by running db.

  ```shell
  db
  ```

* Show current databases in existence

  ```shell
  show dbs
  ```

* Create a collection

  ```shell
  db.createCollection("destinations")
  ```

* See all collections in a database

  ```shell
  show collections
  ```

* Insert data into the travel_db database with this command.

    * NOTE: This will also create the collection automatically, the contents of the insert are basically a JavaScript object, and include an array.

  ```shell
  db.destinations.insertOne({"continent": "Africa", "country": "Morocco", "major_cities": ["Casablanca", "Fez", "Marrakech"]})
  ```

* As a class, come up with 3-5 more countries and insert them into the db using the same syntax as above.

  ```shell
  db.destinations.insertOne({"continent": "Europe", "country": "France", "major_cities": ["Paris", "Marseille", "Bordeaux"]})

  db.destinations.insertOne({"continent": "North America", "country": "USA", "major_cities": ["Washington DC", "New York City", "San Francisco"]})
  ```

* Observe where the data was entered in the MongoDB instance (in mongod)

* Find all data in a Collection with `db.[COLLECTION_NAME].find()`

    * The MongoDB \_id was created automatically.

    * This id is specific for each doc in the collection.

    ```shell
    db.destinations.find()
    ```

* Find specific data by matching a field.

  ```shell
  db.destinations.find({"continent": "Africa"})
  db.destinations.find({"country": "Morocco"})
  ```

* Try a few queries with the examples we came up with as a class.

    * Also, pick something that will find more than one entry so we can see how it will return all matches.

    * Find specific data by matching an \_id.

    ```shell
    db.destinations.find({_id: ObjectId("<ID Number Here>")})

    db.destinations.find({_id: ObjectId("5416fe1d94bcf86cd785439036")})
    ```
