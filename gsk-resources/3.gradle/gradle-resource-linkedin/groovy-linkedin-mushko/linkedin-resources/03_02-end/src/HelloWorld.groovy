class HelloWorld {
    static void main(String[] args) {
        Person johnDoe = new Person()
        johnDoe.setFirstName("John")
        johnDoe.setLastName("Doe")
        johnDoe.setAge(40)

        // Create Closure that prints String representation of a person
        Closure personToString = { Person person ->
            println person.toString()
        }

        // Create Closure that prints full name of a person
        Closure personFullName = { Person person ->
            println person.firstName + " " + person.lastName
        }

        // Pass Closure to a method and execute it
        handlePerson(personToString, johnDoe)
        handlePerson(personFullName, johnDoe)
    }

    static void handlePerson(Closure c, Person p) {
        if (p == null) {
            throw new RuntimeException("A person instance cannot be null")
        }

        c(p)
    }
}