import groovy.transform.Canonical

// Declare convenience annotations on class-level
@Canonical
class Person {
    String firstName
    String lastName
    int age
}
