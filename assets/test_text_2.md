---
Completado: Yes
Dificultad: ⭐⭐
Etiquetas: Basico, Estructura, Java, Sintaxis
Fecha: January 1, 2023
Fuentes: https://www.mhe.es/universidad/informatica/8448132904/archivos/general_apendice3.pdf
---

# Sintaxis de Java

## Variables

En Java, existen diferentes tipos de variables, como enteros, flotantes, caracteres y booleanos, además de variables de tipo objeto como String o Arrays. Es importante declarar el tipo de variable correcto para evitar errores en tiempo de ejecución. Por ejemplo, si quieres almacenar un valor numérico entero, se debe utilizar "int" como el tipo de dato.

```java
int numeroEntero = 10;
float decimal = 3.14f;
char letra = 'A';
boolean verdaderoOFalso = true;
```

## Variables dinámicas

Java es un lenguaje de tipado estático, lo que significa que el tipo de datos de una variable se debe especificar en tiempo de compilación. Sin embargo, existe una forma de crear variables que pueden almacenar diferentes tipos de datos en tiempo de ejecución utilizando la clase "_Object_".

```java
Object variableDinamica = "Hola mundo!";
// En este momento, la variable puede almacenar cualquier tipo de objeto, incluyendo una cadena.

variableDinamica = 100;
// Ahora la variable esta almacenando un valor numerico.
```

> Ten en cuenta que al trabajar con variables dinámicas se debe de tener cuidado al momento de realizar operaciones o acceder a los métodos ya que pueden generar errores en tiempo de ejecución si no se realizan las conversiones adecuadas.

## Tipo de dato string

En Java, una variable de tipo _String_ es un objeto que almacena una cadena de caracteres. Puedes crear una variable de tipo String de varias maneras.

Utilizando el constructor vacío de la clase String:

```java
String s1 = new String();
```

Utilizando una cadena literal:

```java
String s2 = "Hola mundo";
```

Utilizando un arreglo de caracteres:

```java
char[] arr = {'H','o','l','a',' ','m','u','n','d','o'};
String s3 = new String(arr);
```

En estos casos, la variable "s1" es una cadena vacía, la variable "s2" es una cadena con el valor "Hola mundo" y la variable "s3" es una cadena cuyos caracteres son los elementos del arreglo arr.

> Es importante mencionar que en java, las cadenas son inmutables es decir una vez se crea una cadena no se puede modificar sus valores, pero se pueden concatenar y crear nuevas cadenas con valores diferentes a partir de la original.
>
> ```java
> String saludo = "Hola";
> String nombre = "Juan";
> String mensaje = saludo + " " + nombre;
> System.out.println(mensaje);  // imprime "Hola Juan"
> ```
>
> En este caso se crea una variable "mensaje" que es una nueva cadena que se construye mediante la concatenación de las variables "saludo" y "nombre" separadas por un espacio.

Como se mencionó anteriormente, las cadenas (String) en Java son inmutables, lo que significa que una vez creada, no se puede cambiar su contenido. Sin embargo, se pueden crear nuevas cadenas a partir de una cadena existente, mediante la concatenación de otros caracteres o cadenas.

```java
String s = "Hola";
s = s + " mundo";  // se crea una nueva cadena "Hola mundo" y se asigna a la variable s
```

En este ejemplo, la primera línea crea una cadena con el valor "Hola". La segunda línea crea una nueva cadena que es la concatenación de la cadena original "Hola" y el caracter " mundo", y asigna la nueva cadena a la variable "s".

En este ejemplo, la primera línea crea una cadena con el valor "Hola". La segunda línea crea una nueva cadena que es la concatenación de la cadena original "Hola" y el caracter " mundo", y asigna la nueva cadena a la variable "s".

```java
StringBuilder sb = new StringBuilder("Hola");
sb.append(" mundo");
String s = sb.toString();
```

En este ejemplo, la clase StringBuilder se utiliza para construir una cadena modificable. Con el metodo append() se concatena a la cadena "Hola" el caracter " mundo" y con el metodo toString() se vuelve a convertir en una cadena tradicional.

Es importante mencionar que el uso de StringBuilder es más eficiente en casos en los que se deben realizar varias modificaciones en una cadena, ya que al ser mutable no requiere la creación de nuevos objetos de cadena cada vez que se realiza una modificación.

## Funciones

En Java, las funciones se conocen como métodos y son parte de una clase. Los métodos tienen una lista de parámetros y un cuerpo de código que se ejecuta cuando se llama el método. También pueden retornar un valor. El siguiente ejemplo es un método que toma dos números como parámetros y retorna su suma:

```java
public int sumar(int a, int b) {
    return a + b;
}
```

## Funciones sin retorno o dinámicas

Por defecto, todas las funciones en Java deben retornar un valor o indicar que no retornarán nada utilizando la palabra reservada "_void_" en su declaración. Sin embargo, también es posible utilizar la clase "_Object_" para crear funciones que pueden retornar diferentes tipos de datos en tiempo de ejecución:

```java
public Object miFuncion() {
    if(someCondition) {
        return "Hello World";
    } else {
        return 100;
    }
}
```

También es posible crear funciones que no retornen ningún valor utilizando la palabra reservada "_void_”.

```java
public void miFuncion(){
  //cuerpo de la función
}
```

> Es importante tener en cuenta que al trabajar con funciones que no retornan nada o que no se sabe que retornarán, se debe tener cuidado al momento de asignar el valor retornado, ya que puede generar errores.

## Operadores Lógicos

Los operadores lógicos se utilizan para comparar dos o más valores y determinar si una afirmación es verdadera o falsa. Java proporciona los operadores lógicos comunes como _"&&" (and), "||" (or) y "!" (not)_. El siguiente ejemplo utiliza el operador lógico "&&" para verificar si dos números son mayores que cero:

```java
int num1 = 2;
int num2 = 1;

// Mayor que
System.out.println(num1 > num2); // true

// Menor que
System.out.println(num1 < num2); // false

// Mayor o igual que
System.out.println(num1 >= num2); // true

// Menor o igual que
System.out.println(num1 <= num2); // false

// Igual que
System.out.println(num1 == num2); // false

// Diferente que
System.out.println(num1 != num2); // true
```

```java
boolean a = true;
boolean b = false;

// && (AND) retorna true si ambas condiciones son true
System.out.println(a && b); // false

// || (OR) retorna true si al menos una de las condiciones es true
System.out.println(a || b); // true

// ! (NOT) retorna el valor opuesto de la condición
System.out.println(!a); // false
```

- El operador && (AND) evalúa si ambas condiciones son true o ambas son false y retorna true si es así, de lo contrario retorna false.
- El operador || (OR) evalúa si al menos una de las condiciones es true y retorna true si es así, de lo contrario retorna false.
- El operador ! (NOT) retorna el valor opuesto de la condición, es decir si la condición es true, retorna false y viceversa.

## Condicionales

Java proporciona estructuras de control de flujo para controlar el flujo de ejecución de un programa. La estructura "if-else" permite tomar decisiones en función de una condición dada. En el siguiente ejemplo, se utiliza la estructura "if-else" para verificar si un número es par o impar:

```java
if (numero % 2 == 0) {
    System.out.println("El número es par.");
} else {
    System.out.println("El número es impar.");
}
```

## Condicional else if

La estructura "if-else" en Java permite tomar decisiones en función de una condición dada. Sin embargo, en algunos casos es necesario evaluar varias condiciones antes de tomar una decisión. Es aquí donde entra en juego la estructura "else if". La estructura "else if" permite agregar múltiples condiciones adicionales que se evalúan si la condición principal (if) es falsa.

```java
if(condition1) {
    // código a ejecutar si condition1 es verdadera
} else if (condition2) {
    // código a ejecutar si condition1 es falsa y condition2 es verdadera
} else if (condition3) {
    // código a ejecutar si condition1 y condition2 son falsas y condition3 es verdadera
} else {
    // código a ejecutar si todas las condiciones son falsas
}
```

> Es importante tener en cuenta que solo una de las condiciones será verdadera, cuando una condición es verdadera, el código dentro de ese bloque se ejecuta y el resto de las condiciones se ignoran, por lo que no es necesario incluir sentencia "break" o "return" al final de cada bloque de código.

> Es importante que la estructura "else if" no sea confundida con la estructura "switch-case", aunque ambas sirven para seleccionar una de varias acciones, las condicionales "else if" se basan en evaluar una serie de condiciones mientras que la estructura "switch-case" se basa en comparar una expresión especifica a una serie de valores.

## Condicional Switch

La estructura "switch-case" se utiliza para seleccionar una de varias acciones en función de una expresión. En el siguiente ejemplo, se utiliza "switch-case" para elegir una acción en función del valor de una variable:

```java
int opcion = 2;
switch(opcion) {
    case 1:
        System.out.println("Seleccionó la opción 1.");
        break;
    case 2:
        System.out.println("Seleccionó la opción 2.");
        break;
    default:
        System.out.println("Opción inválida.");
}
```

## Bucles

Java proporciona diferentes estructuras de control de bucles para repetir un bloque de código varias veces, como "_for_" y "_while_". El bucle "_for_" se utiliza para iterar un bloque de código un número específico de veces. En el siguiente ejemplo, se utiliza un bucle "_for_" para imprimir los números del 1 al 10:

```java
for(int i = 1; i <= 10; i++) {
    System.out.println(i);
}
```

El bucle "_while_" se utiliza para repetir un bloque de código mientras se cumpla una condición. En el siguiente ejemplo, se utiliza un bucle "while" para imprimir los números del 1 al 10:

```java
int i = 1;
while(i <= 10) {
    System.out.println(i);
    i++;
}
```

El bucle "do-while" es similar al bucle "while", ya que ambos se utilizan para repetir un bloque de código mientras se cumpla una condición. Sin embargo, la principal diferencia entre estos dos bucles es que el "do-while" garantiza que el bloque de código dentro del bucle se ejecutará al menos una vez antes de evaluar la condición. La sintaxis del bucle "do-while" se ve así:

```java
do {
   // bloque de código a ejecutar
} while (condition);
```

En el siguiente ejemplo, se utiliza un bucle "_do-while_" para pedir al usuario que ingrese un número y se verifica si el número es mayor que cero. El bucle se ejecuta mientras el número sea menor o igual a cero.

```java
int numero;
do {
   numero = scanner.nextInt();
   System.out.println("Ingrese un número mayor a cero");
} while (numero <= 0);
```

> Es importante tener en cuenta que, debido a que la condición se evalúa después de la ejecución del código dentro del bucle, siempre se ejecutará al menos una vez el bloque de código dentro del bucle.

En algunos casos, es mejor utilizar un bucle "while" en lugar de un "do-while" y viceversa, depende del escenario o la lógica del problema que se quiere resolver.

>

## Detener Bucles

Hay varias maneras de detener un bucle en Java, una de las más comunes es utilizar la instrucción "_break_" dentro del bloque de código del bucle. La instrucción "_break_" interrumpe la ejecución del bucle actual y continúa la ejecución del código después del bucle.

```java
while(condition) {
   if(stopCondition) {
       break;
   }
   // código a ejecutar
}
```

En el siguiente ejemplo, se utiliza un bucle "while" para imprimir los números del 1 al 10, pero se detiene cuando el número llega a 5:

```java
int i = 1;
while(i <= 10) {
   if(i==5) {
       break;
   }
   System.out.println(i);
   i++;
}
```

Otra manera de detener un bucle es utilizando la instrucción "_return_" dentro del bloque de código del bucle, esta detiene la ejecución del bucle y del método en el que se encuentra.

```java
while(condition) {
   if(stopCondition) {
       return;
   }
   // código a ejecutar
}
```

Otra manera es utilizando una variable booleana para controlar el estado del bucle, es una forma de seguir en ejecución hasta que una condición específica sea cumplida.

```java
boolean ejecutando = true;
while(ejecutando) {
   if(stopCondition) {
       ejecutando=false;
   }
   // código a ejecutar
}
```

> Es importante elegir la forma de detener un bucle de acuerdo a la lógica y necesidad de tu programa, para evitar causar errores en el flujo de ejecución de tu programa.

## Arreglos de datos

En Java, los arreglos son objetos especiales que permiten almacenar un conjunto de elementos del mismo tipo. Se pueden crear de dos maneras: mediante la instrucción "new" o mediante una lista de elementos literales.

### Creación mediante la instrucción "new":

```java
int[] arr1; //declaración del arreglo
arr1 = new int[5]; //creación del arreglo con 5 elementos
```

o también se puede hacer en una sola línea:

```java
int[] arr1 = new int[5];
```

En este caso, se está creando un arreglo de enteros con 5 elementos. Todos los elementos del arreglo se inicializan con su valor por defecto (0 para tipos numéricos como int, false para boolean, null para objetos, etc.).

### Creación mediante una lista de elementos literales:

```java
int[] arr2 = {1, 2, 3, 4, 5};
```

En este caso, se está creando un arreglo de enteros con los elementos 1, 2, 3, 4 y 5.

En ambos casos, una vez creado el arreglo, los elementos se pueden acceder mediante el uso de los corchetes []:

```java
arr1[0] = 1; // asigna el valor 1 al primer elemento del arreglo
int x = arr1[0]; // asigna el valor del primer elemento del arreglo a la variable x
```

> Es importante notar que también se pueden crear arreglos de objetos y otros tipos de datos.
>
> ```java
> String[] nombres = new String[5];
> nombres[0] = "Lucas";
> nombres[1] = "Juan";
> nombres[2] = "Maria";
> nombres[3] = "Ana";
> nombres[4] = "Pedro";
> ```
>
> En este ejemplo se crea un arreglo de 5 elementos de tipo String, y se les asigna un valor a cada uno de ellos.

## Arreglos de longitud dinamica

En algunos casos puede ser necesario crear un arreglo cuyo tamaño no se conoce previamente, es decir, dinámico. Una forma de hacer esto en Java es utilizando una estructura de datos llamada ArrayList, que es parte de la biblioteca estándar de Java y permite almacenar elementos de cualquier tipo en una lista que se puede ir ajustando automáticamente a medida que se añaden o quitan elementos.

Para utilizar un ArrayList se necesita importar la clase:

```java
import java.util.ArrayList;
```

Para crear un ArrayList se utiliza el constructor vacío:

```java
ArrayList<TipoDeDato> nombreLista = new ArrayList<TipoDeDato>();
```

Un ejemplo de esto seria el siguiente

```java
import java.util.ArrayList;

public class EjemploArrayList {

   public static void main(String[] args) {
      ArrayList<String> nombres = new ArrayList<String>();
      nombres.add("Lucas");
      nombres.add("Juan");
      nombres.add("Maria");
      nombres.add("Ana");
      nombres.add("Pedro");
      System.out.println(nombres);
   }
}
```

En este ejemplo, se crea un ArrayList llamado nombres, y se agrega algunos elementos de tipo String utilizando el método add(). El tamaño del ArrayList se ajusta automáticamente de acuerdo a la cantidad de elementos que se añaden.

Es importante mencionar que desde java 8 existe una forma más concisa para crear un ArrayList, mediante el uso de la clase Collections.

```java
List<String> nombres = new ArrayList<>(Arrays.asList("Lucas", "Juan","Maria","Ana","Pedro"));
```

En este caso se crea un ArrayList llamado nombres con varios elementos de tipo String.

También se pueden utilizar otras clases similares como LinkedList o Vector.
