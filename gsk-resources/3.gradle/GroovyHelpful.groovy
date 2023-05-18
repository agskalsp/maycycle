int a =10
def a=20
float a = 10.22F

println a
println a.class

s= 'hello'
// "" has ${} usage where as '' don't have it
USER= ubuntu
s= "Hello ${USER}"
print s

s= '''
This a longer string with three appostrope's
at start and three appostrope's
at end
'''
println(s)

emailPattern = "user@gmail.com"
println "user@gmail.com"==~ emailPattern
// .class or .getClass both work same
println emailPattern.getClass()
//  ==~ is used for checking conditions

// Closures
c= {  n=3 ->
      println(n%2 ? "even" : "odd")
}
c.call()
c.call(100)

4.times { n -> println n}
4.times { println it}

//Collections

l1 = [1,2,3,4]
LinkedList l2 = [3,7,2,1]
println l1.class
println l2.class

l1 << 5
l1 = l1 + [6,7,8]
println l1- [3,4]

l1.each  { println it}
l1.reverseEach  { println it}
l1.eachPermutation  { println it}
l1.eachCombination  { println it}

// Sets and Maps

s = ['java', 'js', 'python', 'js' ] as Set
println s.class --> it gives a LinkedHashSet
TreeSet s1 = ['java', 'js', 'python', 'js' ] as Set
println s1.class

m= [courseName: 'Gradle', rating: 5, price: 50.99]
println m
m.each{
    k,v ->
    println k
    println v
}

println m.courseName
println m[courseName]
println m.get(courseName)

m['review']= "It's good"
println m.get('review')  // it might even be this syntax as well check m.get(review) 


//  Methods
int product(int x, int y)
{
    return x*y
}
println product(4,5)

def product(int x=8, int y)
{
    x*y
}
result = product 9
println result

void display(Map productDetails){
    println productDetails.name
    println productDetails.price
}

display([name:'Iphone',price:1000])

// Classes

package com.bharath.groovy

class Patient {
def firstName, lastName, age 
static hospitalCode="Best Hospital"
    void setLastName (lastName) {
      if(lastName=null) {
           throw new IllegalArgumentException("Last Name can not be null");
        }
      this.lastName=lastName
    }
    static void display() { 
        println hospitalCode
    }
}
p=new Patient (firstName: 'John', lastName: 'Bailey', age:40)
p.setLastName("Buffer")
println p.firstName+" "+p. lastName+" "+p.age
Patient.display()