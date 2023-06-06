class HelloWorld {
    static void main(String[] args) {
        Person johnDoe = new Person()
        johnDoe.setFirstName("John")
        johnDoe.setLastName("Doe")
        johnDoe.setAge(40)

        // Use the dropRight method to remove 2 characters from the end
        println johnDoe.getFirstName().dropRight(2)
    }
}