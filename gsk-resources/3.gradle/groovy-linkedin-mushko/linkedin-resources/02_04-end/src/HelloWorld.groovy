class HelloWorld {
    static void main(String[] args) {
        Person johnDoe = new Person()
        johnDoe.setFirstName("John")
        johnDoe.setLastName("Doe")
        johnDoe.setAge(40)
        println johnDoe.getFullName()
        println johnDoe.getAge()

        // Identify if Person is middle-aged using a conditional
        if (johnDoe.getAge() >= 45 && johnDoe.getAge() <= 65) {
            println johnDoe.getFullName() + " is a middle-aged person"
        } else {
            println johnDoe.getFullName() + " is " + johnDoe.getAge() + " years old"
        }

        // Define a list of Persons
        def persons = [johnDoe, new Person(firstName: "Mary", lastName: "Hill")]

         // Iterate over Person instances in list
        for (Person p : persons) {
            println "Person: " + p.getFullName()
        }
    }
}