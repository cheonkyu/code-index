# Item 42: `compareTo` 계약을 존중하라

안녕하세요! 코틀린 프로그래밍 전문가로서 `compareTo` 함수에 대한 중요한 규칙을 설명해 드릴게요. `compareTo`는 객체들을 비교하고 정렬하는 데 핵심적인 역할을 하는 함수인데, 이 함수의 계약을 제대로 지키지 않으면 예기치 않은 문제가 발생할 수 있답니다.

## `compareTo` 함수란 무엇인가요?

`compareTo` 함수는 `Comparable` 인터페이스를 구현하는 클래스에서 사용됩니다. 이 함수는 두 객체를 비교하여 다음과 같은 값을 반환합니다.

*   **음수:** 호출한 객체가 `compareTo` 함수의 인자로 전달된 객체보다 작을 경우
*   **0:** 두 객체가 같을 경우
*   **양수:** 호출한 객체가 `compareTo` 함수의 인자로 전달된 객체보다 클 경우

이 반환 값을 통해 객체들은 정렬될 수 있습니다. 예를 들어, 문자열을 사전순으로 정렬하거나 숫자를 오름차순 또는 내림차순으로 정렬할 때 `compareTo` 함수가 활용됩니다.

## `compareTo` 계약 (Contract)이란 무엇이며 왜 중요할까요?

`compareTo` 함수는 단순한 비교 함수가 아니라, 특정 규칙(계약)을 따라야 합니다. 이 계약을 지키지 않으면 정렬 알고리즘이 제대로 작동하지 않거나, 예상치 못한 오류가 발생할 수 있습니다. 주요 계약 내용은 다음과 같습니다.

1.  **대칭성 (Symmetry):** `a.compareTo(b)` 와 `b.compareTo(a)`는 서로 반대 부호이거나 0이어야 합니다. 즉, `a < b` 이면 `b > a`가 되어야 합니다.
2.  **전이성 (Transitivity):** `a.compareTo(b) < 0` 이고 `b.compareTo(c) < 0` 이면, `a.compareTo(c) < 0` 이어야 합니다. 즉, `a < b` 이고 `b < c` 이면 `a < c` 가 되어야 합니다.
3.  **동일성 (Identity):** `a.compareTo(a)` 는 항상 0이어야 합니다. 즉, 자기 자신과 비교하면 항상 같다고 판단해야 합니다.
4.  **null 안전성:** `compareTo`를 구현할 때 `null` 값을 어떻게 처리할지 명확히 정의해야 합니다.  코틀린에서는 `Comparable` 인터페이스에 `null` 비교에 대한 명시적인 규칙은 없지만, 일관성 있는 동작을 위해 처리하는 것이 좋습니다.

## `compareTo` 계약 위반 시 발생하는 문제

계약을 위반하면 정렬 결과가 불안정해지거나, 예상치 못한 오류가 발생할 수 있습니다. 예를 들어, 대칭성이 위반되면 정렬 알고리즘이 무한 루프에 빠질 수도 있습니다.

## 예제: `compareTo` 계약을 올바르게 구현하는 방법

다음은 간단한 `Person` 클래스를 예제로 들어 `compareTo` 함수를 올바르게 구현하는 방법을 보여줍니다. 이름으로 정렬하도록 구현합니다.

```kotlin
data class Person(val name: String, val age: Int) : Comparable<Person> {
    override fun compareTo(other: Person): Int {
        return name.compareTo(other.name)
    }
}

fun main() {
    val people = listOf(
        Person("Alice", 30),
        Person("Bob", 25),
        Person("Charlie", 35)
    )

    val sortedPeople = people.sorted()
    println(sortedPeople) // 출력: [Person(name=Alice, age=30), Person(name=Bob, age=25), Person(name=Charlie, age=35)]
}
```

이 예제에서 `compareTo` 함수는 `name` 속성을 사용하여 두 `Person` 객체를 비교합니다.  `String` 클래스의 `compareTo` 함수를 활용하여 대칭성, 전이성, 동일성을 자동으로 만족시킵니다.

## 예제: `compareTo` 계약을 위반하는 경우

다음은 `compareTo` 계약을 위반하는 잘못된 예제입니다.

```kotlin
data class FaultyPerson(val name: String, val age: Int) : Comparable<FaultyPerson> {
    override fun compareTo(other: FaultyPerson): Int {
        if (age > other.age) {
            return -1 // 대칭성 위반!
        } else if (age < other.age) {
            return 1 // 대칭성 위반!
        } else {
            return 0
        }
    }
}

fun main() {
    val people = listOf(
        FaultyPerson("Alice", 30),
        FaultyPerson("Bob", 25),
        FaultyPerson("Charlie", 35)
    )

    val sortedPeople = people.sorted()
    println(sortedPeople) // 예상치 못한 결과가 나올 수 있음
}
```

이 예제에서 `compareTo` 함수는 나이 속성을 사용하여 비교하지만, 결과의 부호가 잘못되어 대칭성을 위반합니다.  이러한 경우 정렬 결과가 예상과 다르게 나올 수 있습니다.

## 핵심 요약

*   `compareTo` 함수는 `Comparable` 인터페이스를 구현하는 클래스에서 객체 비교 및 정렬에 사용됩니다.
*   `compareTo` 함수는 대칭성, 전이성, 동일성 등의 계약을 준수해야 합니다.
*   계약을 위반하면 정렬 결과가 불안정해지거나, 예기치 않은 오류가 발생할 수 있습니다.
*   `compareTo` 함수를 구현할 때, 신중하게 계약을 고려하고, 가능한 한 기존의 비교 함수 (예: `String.compareTo()`)를 활용하는 것이 좋습니다.