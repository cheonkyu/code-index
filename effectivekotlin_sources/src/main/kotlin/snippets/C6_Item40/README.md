# Item 40: equals 계약을 존중하라

안녕하세요! 코틀린 프로그래밍을 공부하시는 여러분을 위해 Effective Kotlin의 Item 40, "equals 계약을 존중하라"에 대해 자세히 설명해 드리려고 합니다. `equals()` 메서드는 객체 비교에 중요한 역할을 하는데, 이 메서드를 올바르게 구현하지 않으면 예상치 못한 오류가 발생할 수 있어요. 이 아이템에서는 `equals()` 메서드의 작동 방식과 어떻게 올바르게 구현해야 하는지 함께 살펴보겠습니다.

## equals() 계약이란 무엇일까요?

`equals()` 메서드는 객체 비교를 위한 계약(contract)을 가지고 있습니다. 이 계약은 `equals()` 메서드를 사용하는 코드의 정확성을 보장하기 위해 지켜져야 하는 규칙들을 의미합니다. 이 계약을 제대로 지키지 않으면, 객체가 제대로 비교되지 않거나, 컬렉션(HashSet, HashMap 등)에서 예상치 못한 동작이 발생할 수 있습니다.

`equals()` 계약은 크게 세 가지 규칙으로 구성됩니다.

1. **반사성 (Reflexivity):** 모든 객체 `x`에 대해 `x.equals(x)`는 `true`를 반환해야 합니다. 즉, 자기 자신과 비교하면 항상 같아야 한다는 뜻입니다.

2. **대칭성 (Symmetry):** 객체 `x`와 `y`에 대해 `x.equals(y)`가 `true`라면, `y.equals(x)`도 `true`여야 합니다. 즉, 두 객체가 같다면 순서를 바꿔서 비교해도 같아야 합니다.

3. **추이성 (Transitivity):** 객체 `x`, `y`, `z`에 대해 `x.equals(y)`가 `true`이고 `y.equals(z)`가 `true`라면, `x.equals(z)`도 `true`여야 합니다. 즉, x가 y와 같고 y가 z와 같다면 x는 z와도 같아야 합니다.

## equals() 메서드 오버라이딩 시 주의 사항

코틀린에서 `equals()` 메서드를 오버라이딩할 때는 다음과 같은 사항에 주의해야 합니다.

* **hashCode() 메서드도 함께 오버라이딩해야 합니다.** `equals()` 메서드를 오버라이딩하면 `hashCode()` 메서드도 반드시 오버라이딩해야 합니다.  `equals()`가 `true`를 반환하는 두 객체는 반드시 동일한 `hashCode` 값을 가져야 합니다. 이는 컬렉션(HashMap, HashSet 등)이 객체를 효율적으로 관리하기 위한 필수 조건입니다.  만약 `equals()`를 오버라이딩했지만 `hashCode()`를 오버라이딩하지 않으면, 컬렉션의 동작이 예상과 다를 수 있습니다.

* **동일성 비교 기준을 명확히 정의해야 합니다.** 어떤 속성을 기준으로 두 객체를 같은 객체로 간주할 것인지 명확하게 정의해야 합니다.  객체의 모든 속성이 같을 때만 `true`를 반환할 수도 있고, 특정 속성만 같을 때 `true`를 반환할 수도 있습니다.  어떤 기준을 사용할지는 설계 의도에 따라 결정됩니다.

* **null 값 처리에 유의해야 합니다.**  `equals()` 메서드에 `null` 값이 전달될 수 있으므로, `null` 값에 대한 처리를 적절하게 수행해야 합니다. 예를 들어, 현재 객체가 `null`인 경우 `false`를 반환하거나, 비교 대상 객체가 `null`인 경우에도 `false`를 반환할 수 있습니다.

## 예제 코드

다음은 `equals()`와 `hashCode()` 메서드를 함께 오버라이딩하는 예제 코드입니다.

```kotlin
data class Person(val name: String, val age: Int) {
    // equals() 와 hashCode() 를 함께 오버라이딩
    override fun equals(other: Any?): Boolean {
        if (this === other) return true  // 자기 자신 비교
        if (other !is Person) return false // 타입 확인
        return name == other.name && age == other.age // 속성 비교
    }

    override fun hashCode(): Int {
        return name.hashCode() + age.hashCode() // 속성을 사용하여 해시 코드 생성
    }
}

fun main() {
    val person1 = Person("Alice", 30)
    val person2 = Person("Alice", 30)
    val person3 = Person("Bob", 25)

    println(person1.equals(person2)) // true
    println(person1.equals(person3)) // false
    println(person1.hashCode() == person2.hashCode()) // true
    println(person1.hashCode() == person3.hashCode()) // false
}
```

위 예제에서 `Person` 클래스는 `name`과 `age` 두 개의 속성을 가지고 있습니다. `equals()` 메서드는 `name`과 `age`가 모두 같은 경우에만 `true`를 반환하도록 구현되어 있습니다. 또한, `hashCode()` 메서드는 `name`과 `age`의 해시 코드를 합쳐서 반환하도록 구현되어 있습니다. 이렇게 하면 `equals()`가 `true`를 반환하는 두 객체는 항상 동일한 해시 코드를 가지게 됩니다.

## 핵심 요약

* `equals()` 메서드는 객체 비교를 위한 계약을 가지고 있으며, 이 계약을 존중해야 합니다.
* `equals()` 메서드를 오버라이딩할 때는 반드시 `hashCode()` 메서드도 함께 오버라이딩해야 합니다.
* 동일성 비교 기준을 명확히 정의하고, null 값 처리에 유의해야 합니다.
* `equals()`와 `hashCode()`를 올바르게 구현하면 객체 비교의 정확성을 보장하고 컬렉션의 효율적인 동작을 지원할 수 있습니다.