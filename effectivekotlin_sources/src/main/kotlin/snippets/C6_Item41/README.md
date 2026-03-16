# Item 41: 해시 코드 계약을 존중하라

## 핵심 가이드라인

해시 코드 계약은 객체 지향 프로그래밍에서 중요한 역할을 합니다. **Effective Kotlin**에서 제시하는 핵심 가이드라인은 다음과 같습니다:

1. **일관성 유지**: 같은 객체에 대해 여러 번 `hashCode()`를 호출하더라도 항상 동일한 해시 값을 반환해야 합니다. 이는 객체의 불변성을 유지하는 데 중요합니다.
   
2. **균등성 보장**: 두 객체가 `equals()` 메서드로 동일함이 확인되면, 그들의 `hashCode()` 값도 동일해야 합니다. 반대로, `hashCode()` 값이 동일한 두 객체는 반드시 `equals()`를 통해 동일함을 검증해야 합니다. 하지만, `hashCode()` 값이 같다고 해서 무조건 `equals()`가 동일하다고 단정할 수는 없습니다.

이러한 가이드라인은 컬렉션(특히 `HashMap`, `HashSet`)에서 객체를 효율적으로 관리하는 데 필수적입니다. 해시 충돌을 최소화하고, 객체의 정확한 검색과 분류를 가능하게 합니다.

## 이유 (Best Practice)

- **효율적인 검색**: 해시 코드를 제대로 구현하면 `HashMap`이나 `HashSet`과 같은 해시 기반 컬렉션에서 객체의 검색 속도가 크게 향상됩니다.
- **정확성**: 일관성과 균등성을 지키면 객체의 정확한 식별과 그룹화가 가능해져 프로그램의 안정성이 높아집니다.
- **예측 가능성**: 개발자가 예상한 동작을 일관되게 보장함으로써 코드의 예측 가능성을 높입니다.

## 예제 코드

다음은 간단한 클래스 예시로 `Person` 클래스를 정의하고 `hashCode()` 메서드를 올바르게 구현한 경우입니다.

```kotlin
class Person(val name: String, val age: Int) {
    override fun equals(other: Any?): Boolean {
        if (this === other) return true
        if (other !is Person) return false
        return name == other.name && age == other.age
    }

    override fun hashCode(): Int {
        // 이름과 나이를 기반으로 해시 코드 생성
        return name.hashCode() + age.hashCode()
    }
}

fun main() {
    val person1 = Person("Alice", 30)
    val person2 = Person("Alice", 30)
    
    println("person1 hashCode: ${person1.hashCode()}")  // 출력: person1 hashCode: ...
    println("person2 hashCode: ${person2.hashCode()}")  // 출력: person2 hashCode: ...
    
    // 동일한 객체에 대한 호출은 동일한 해시 값을 반환해야 함
    println("person1과 person2는 동일한가? ${person1 == person2}")  // 출력: true
}
```

위 예제에서는 `Person` 클래스의 `hashCode()` 메서드가 `name`과 `age`를 고려하여 해시 코드를 생성합니다. `equals()` 메서드와 함께 일관성과 균등성을 유지함으로써 올바른 동작을 보장합니다.

## 핵심 요약

- 해시 코드는 객체의 불변성을 유지하고, 동일성 검사에서 중요한 역할을 합니다.
- `hashCode()`는 일관성과 균등성을 지켜야 하며, 이를 통해 효율적인 데이터 관리가 가능합니다.
- 올바른 구현은 프로그램의 안정성과 예측 가능성을 높입니다.