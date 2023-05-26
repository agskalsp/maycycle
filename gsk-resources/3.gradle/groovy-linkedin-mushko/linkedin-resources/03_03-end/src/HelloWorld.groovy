class HelloWorld {
    static void main(String[] args) {
        Person johnDoe = new Person("John", "Doe", 40)
        Person maryHill = new Person("Mary", "Hill", 30)
        Person thomasMarks = new Person("Thomas", "Marks", 21)

        // Create a new list of persons
        def allPersons = [johnDoe, maryHill, thomasMarks]

        // Querying Collections
        assert allPersons instanceof java.util.List
        assert allPersons.size() == 3
        assert allPersons[2] == thomasMarks

        // Iterate over elements
        allPersons.each {
            println it
        }

        // Iterate over elements and using an index
        allPersons.eachWithIndex { person, index ->
            println index + ": " + person
        }

        // Filtering a specific element
        assert allPersons.find { it.lastName == 'Hill' } == maryHill

        // Transforming elements into something else
        assert allPersons.collect { it.age <= 30 } == [false, true, true]

        // Sorting elements based on a criterion
        assert allPersons.sort { it.age } == [thomasMarks, maryHill, johnDoe]
    }
}