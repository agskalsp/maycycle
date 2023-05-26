class Main {
    static void main(String[] args) {
        // Read numbers from files and store them in List
        List<Integer> allNumbers = readAllNumbers()

        // Find the highest number
        Integer maxNumber = allNumbers.max()
        assert maxNumber == 2044

        // Create the sum of all numbers
        Integer sum = allNumbers.sum()
        assert sum == 8180
    }

    private static List<Integer> readAllNumbers() {
        File resourcesDir = new File("resources")
        List<Integer> allNumbers = []

        resourcesDir.eachFile { file ->
            file.eachLine { line ->
                if (line.isNumber()) {
                    allNumbers << line.toInteger()
                }
            }
        }

        allNumbers
    }
}