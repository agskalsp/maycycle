class HelloWorld {
    static void main(String[] args) {
        Person johnDoe = new Person()
        johnDoe.setFirstName("John")
        johnDoe.setLastName("Doe")
        johnDoe.setAge(40)

        // Catch unchecked exception
        try {
            // Convert a String into a Long data type
            johnDoe.getFirstName().toLong()
        } catch (NumberFormatException e) {
            // Handle unchecked exception by printing a message
            assert e instanceof NumberFormatException
            println "Cannot convert a String into a Long"
        }
    }
}