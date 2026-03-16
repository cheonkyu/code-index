# Item 1. 가변성을 제한하라

## 핵심 가이드라인

이 주제는 코틀린 프로그래밍에서 중요한 원칙 중 하나인 **가변성 제한**에 대해 다룹니다. 코드의 안정성과 유지보수성을 높이기 위해 가능한 한 변수의 상태를 변경할 수 없게 만드는 것이 권장됩니다. 이 접근법은 오류 발생 가능성을 줄이고, 코드의 예측 가능성을 향상시키는 데 도움이 됩니다.

### 이유 (Best Practice)
- **오류 감소**: 불변 변수는 상태 변경이 불가능하므로, 의도치 않은 변경으로 인한 버그를 방지합니다.
- **코드 예측성 향상**: 불변 객체는 항상 동일한 상태를 유지하므로, 개발자가 코드의 동작을 더 쉽게 예측할 수 있습니다.
- **멀티스레드 안전성**: 불변 객체는 멀티스레드 환경에서 안전하게 공유할 수 있습니다.

## 예제 코드

다음은 불변 객체와 가변 객체를 사용하는 간단한 예제입니다.

#### 불변 객체 예제
```kotlin
data class Person(val name: String, val age: Int) // 불변 데이터 클래스

fun main() {
    val person = Person("Alice", 30)
    // person.age = 31  // 오류: 오류가 발생하여 속성을 변경할 수 없음
    println(person) // 출력: Person(Alice, 30)
}
```

#### 가변 객체 예제
```kotlin
class PersonMutable {
    var name: String = "" // 가변 속성
    var age: Int = 0   // 가변 속성
}

fun main() {
    val personMutable = PersonMutable()
    personMutable.name = "Bob"
    personMutable.age = 25
    println(personMutable) // 출력: PersonMutable(Bob, 25)
    // 주의: 이러한 변경 가능성은 오류 발생 위험을 증가시킬 수 있습니다.
}
```

## 핵심 요약
- **불변 변수 사용**: 안정성과 예측성을 높여 오류를 줄입니다.
- **가변 변수 최소화**: 특히 멀티스레드 환경에서는 신중하게 사용해야 합니다.
- **코드 유지보수 향상**: 불변성을 통해 코드의 이해와 수정이 훨씬 쉬워집니다.