class HelloWorld {
    static void main(String[] args) {
        // Create new Person class and instantiate it
        Person person = new Person()
        person.setFirstName("John")
        person.setLastName("Doe")
        person.setAge(40)

        // Print the full name and age of Person instance
        println person.getFullName()
        println person.getAge()
    }
}