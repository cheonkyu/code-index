# 40. NullableExtensions

안녕하세요! 코틀린 초보자 여러분, 오늘은 `NullableExtensions`에 대해 배워볼게요. 이 주제는 특히 어떤 변수가 `null` 값을 가질 수 있는지 처리하는 방법에 대해 알아볼 거예요. 코틀린에서 `null`은 객체가 존재하지 않을 때를 나타내는 중요한 개념이죠. `NullableExtensions`는 이런 `null` 처리를 좀 더 안전하고 쉽게 해주는 몇 가지 유용한 확장 함수들을 제공해요.

## 핵심 개념 요약

1. **null 안전 프로그래밍**: 코틀린은 기본적으로 `null`을 처리하는 데 매우 주의를 기울이는데, `NullableExtensions`는 이런 안전한 프로그래밍을 더욱 강화해줘요.
2. **안전한 호출**: `null` 값일 때 메소드 호출이나 연산을 안전하게 처리할 수 있게 도와줘요. 예를 들어, `?.` 연산자와 함께 사용하면 `null`일 때 예외를 일으키지 않고 안전하게 처리할 수 있어요.
3. **확장 함수**: `NullableExtensions`는 기존 함수에 추가적인 `null` 관련 기능을 제공해요. 이를 통해 코드를 더 간결하고 읽기 쉽게 만들 수 있어요.

## 예제 코드 설명

### 1. 안전한 호출 연산자 (Safe Call Operator: `?.`)

`null` 값일 때 메소드를 호출하는 대신 안전하게 처리할 수 있어요. 만약 객체가 `null`이라면 아무 일도 일어나지 않아요.

```kotlin
fun printNameSafe(name: String?) {
    // 이름이 null이면 안전하게 처리
    name?.let { println("이름은 ${it}입니다.") }  // 만약 name이 null이라면 이 부분은 건너뛰어짐
    else {
        println("이름이 없습니다.")
    }
}

fun main() {
    val nullName: String? = null
    printNameSafe(nullName)  // 출력: 이름이 없습니다.

    val validName: String = "김철수"
    printNameSafe(validName)  // 출력: 이름은 김철수입니다.
}
```

### 2. 확장 함수 사용 예시

`NullableExtensions`에서 제공하는 몇 가지 확장 함수를 사용해 보겠습니다. 예를 들어, `orEmpty()` 함수는 `null`인 경우 빈 리스트를 반환해요.

```kotlin
import kotlin.jdk.java.util.*

fun printItemsOrEmpty() {
    val items: List<String>? = null
    println("사용 가능한 아이템: ${items?.orEmpty()}")  // items가 null이므로 빈 리스트 출력

    val nonNullItems: List<String> = listOf("책", "펜")
    println("사용 가능한 아이템: ${nonNullItems.orEmpty()}")  // 리스트 그대로 출력
}

fun main() {
    printItemsOrEmpty()
    // 출력:
    // 사용 가능한 아이템: []
    // 사용 가능한 아이템: [책, 펜]
}
```

### 간단 요약

- **`?.` 연산자**: `null` 값에 대해 안전하게 메소드 호출을 시도해요.
- **확장 함수**: 예를 들어 `orEmpty()`는 `null`을 처리할 때 유용한 기능을 추가해요.

이렇게 `NullableExtensions`를 활용하면 코드가 더 안전하고 읽기 쉬워져요. 코틀린의 강력한 타입 시스템과 함께 이 기능들을 잘 활용하면, `null` 관련 오류를 줄이고 효율적인 코드를 작성할 수 있답니다. 연습해보면서 점차 익숙해질 거예요! 궁금한 점이 있으면 언제든지 물어봐 주세요. 😊