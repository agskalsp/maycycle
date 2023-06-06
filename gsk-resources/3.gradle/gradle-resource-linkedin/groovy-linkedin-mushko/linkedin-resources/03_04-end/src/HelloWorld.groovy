class HelloWorld {
    static void main(String[] args) {
        Person johnDoe = new Person()

        // Read full contents of file
        File file = new File("resources/john-doe.txt")
        String content = file.getText('UTF-8')
        println content

        // Iterate over each line of file
        file.eachLine { line, no ->
            if (no == 1) {
                johnDoe.setFirstName(line)
            } else if (no == 2) {
                johnDoe.setLastName(line)
            } else if (no == 3) {
                johnDoe.setAge(line.toInteger())
            } else {
                throw new RuntimeException("A person text file should only have 3 lines")
            }
        }

        println johnDoe
    }
}