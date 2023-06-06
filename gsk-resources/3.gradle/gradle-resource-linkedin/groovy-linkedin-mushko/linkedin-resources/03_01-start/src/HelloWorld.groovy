class HelloWorld {
    static void main(String[] args) {
        Person johnDoe = new Person()
        johnDoe.setFirstName("John")
        johnDoe.setLastName("Doe")
        johnDoe.setAge(40)

        assert johnDoe.toString() == "Person(John, Doe, 40)"
        assert johnDoe.equals(johnDoe)
        assert !johnDoe.equals(new Person(firstName: "Mary", lastName: "Hill", age: 30))
        assert new Person("Mary", "Hill", 30).toString() == "Person(Mary, Hill, 30)"
    }
}