# Item 21: 프로퍼티 위임을 활용하여 공통 프로퍼티 패턴을 추출하라

안녕하세요! 코틀린 프로그래밍을 더욱 효과적으로 만들어줄 Item 21에 대해 함께 알아볼 거예요. 이 아이템에서는 프로퍼티 위임을 통해 코드 중복을 줄이고, 더 깔끔하고 유지보수하기 쉬운 코드를 작성하는 방법을 다룹니다. 마치 레고 블록처럼, 자주 사용하는 프로퍼티 패턴을 재사용 가능한 형태로 만들어 사용하는 것이죠!

## 프로퍼티 위임이란 무엇일까요?

프로퍼티 위임은 어떤 클래스가 프로퍼티에 대한 접근을 다른 객체에 *위임*하는 것을 의미합니다. 즉, 프로퍼티의 `get()`과 `set()` 동작을 다른 객체가 대신 처리하게 하는 것이죠.  이 기능을 사용하면 클래스 내에서 반복되는 프로퍼티 로직을 제거하고, 해당 로직을 별도의 객체로 분리하여 재사용할 수 있습니다.

## 왜 프로퍼티 위임을 사용해야 할까요? (Best Practice)

* **코드 중복 감소:** 여러 클래스에서 동일한 방식으로 프로퍼티를 관리해야 할 때, 중복된 코드를 제거할 수 있습니다.
* **관심사 분리:** 프로퍼티의 접근 로직을 클래스에서 분리하여, 클래스의 핵심 역할에 집중할 수 있도록 도와줍니다.
* **유지보수 용이성 향상:** 프로퍼티 접근 로직을 수정해야 할 경우, 위임 객체만 변경하면 되므로 전체 코드 수정 범위를 줄일 수 있습니다.
* **가독성 향상:**  복잡한 프로퍼티 로직을 별도로 분리함으로써 코드를 더 명확하게 만들 수 있습니다.

## 프로퍼티 위임의 방법: `by` 키워드

코틀린에서는 `by` 키워드를 사용하여 프로퍼티 위임을 간단하게 구현할 수 있습니다. `by` 키워드 뒤에 위임을 처리할 객체를 지정하면 됩니다.

```kotlin
// 위임을 처리할 객체 (Delegation Provider)
class LoggedProperty(val propertyName: String) {
    operator fun getValue(thisRef: Any?, property: kotlin.reflect.KProperty<*>) : String {
        println("접근된 프로퍼티: $propertyName")
        return thisRef?.toString() ?: "" // null 안전하게 처리
    }

    operator fun setValue(thisRef: Any?, property: kotlin.reflect.KProperty<*>, value: String) {
        println("프로퍼티 $propertyName 에 값 $value 할당")
    }
}

// 위임을 받는 클래스
class Person(val name: String, var age by LoggedProperty("age"))

fun main() {
    val person = Person("Alice", 30)
    println(person.age) // 접근된 프로퍼티: age, 30 출력
    person.age = 31 // 프로퍼티 age 에 값 31 할당 출력
}
```

위 예제에서 `LoggedProperty`는 프로퍼티에 접근하거나 값을 설정할 때 로그를 출력하는 위임 객체입니다. `Person` 클래스의 `age` 프로퍼티는 `LoggedProperty` 객체를 통해 접근 및 설정 로직을 위임받습니다.  `by` 키워드를 사용하여 위임을 설정했기 때문에 `Person` 클래스에서는 별도의 `get()` 또는 `set()` 메서드를 정의할 필요가 없습니다.

## 표준 라이브러리의 유용한 프로퍼티 위임

코틀린 표준 라이브러리에서도 유용한 프로퍼티 위임을 제공합니다.

* **`Lazy<T>`:**  프로퍼티 값이 처음 접근될 때만 초기화되는 위임입니다. (지연 초기화)
* **`ObservableProperty<T>`:** 프로퍼티 값이 변경될 때마다 이벤트(콜백 함수)를 발생시키는 위임입니다. (데이터 바인딩 등에 유용)
* **`VetoableProperty<T>`:** 프로퍼티 값 변경을 허용하기 전에 특정 조건에 따라 거부할 수 있는 위임입니다.

```kotlin
import kotlin.properties.Delegates

class Configuration {
    var apiUrl by Delegates.vetoable { property, oldValue, newValue ->
        if (newValue.startsWith("http://")) {
            true // 변경 허용
        } else {
            false // 변경 거부
        }
    }
}
```

## 핵심 요약

* 프로퍼티 위임은 코드 중복을 줄이고 유지보수성을 높이는 강력한 기능입니다.
* `by` 키워드를 사용하여 프로퍼티의 `get()` 및 `set()` 동작을 다른 객체에 위임할 수 있습니다.
* 코틀린 표준 라이브러리에서 제공하는 `Lazy`, `ObservableProperty`, `VetoableProperty` 등의 위임을 활용하면 더욱 효율적인 코드를 작성할 수 있습니다.
*  프로퍼티 위임을 적절히 사용하면 깔끔하고 확장 가능한 코드를 만들 수 있습니다.