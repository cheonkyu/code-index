# 39. NonNullAssertions

안녕하세요! 코틀린 프로그래밍을 처음 접하는 분들께 `NonNullAssertions`에 대해 쉽게 설명해 드릴게요. 이 주제는 코드에서 `null` 값이 오지 않는다는 것을 보장하는 방법에 대해 다룹니다. 이해하기 쉽게 단계별로 설명해 보겠습니다.

## 왜 NonNullAssertions가 필요한가요?

코틀린에서는 `null` 안전성을 강조하는데, 이는 프로그램에서 `null` 값이 발생할 때 예상치 못한 오류를 방지하기 위함이에요. `NonNullAssertions`는 함수나 변수가 `null`을 반환하거나 할당하지 않는다는 것을 명시적으로 확인하는 도구랍니다. 이렇게 하면 코드의 안정성이 높아지고 디버깅도 훨씬 수월해져요.

### 핵심 개념 요약

1. **NonNullAssertions 사용 목적**:
   - 함수나 변수가 `null`을 반환하거나 할당하지 않는다는 것을 확인합니다.
   - 컴파일 타임에 `null` 관련 오류를 잡아냅니다.

2. **주요 키워드**:
   - `assertNotNull`: 변수나 반환값이 `null`이 아님을 확인합니다.
   - `assert`: 코틀린에서 `null` 안전성을 강화하기 위한 특수 어노테이션입니다.

## 예제 코드로 이해하기

아래 예제를 통해 어떻게 `NonNullAssertions`를 사용하는지 살펴보겠습니다.

### 기본 예제: 변수에 대한 assertNotNull 사용

```kotlin
import kotlin.test.* // 테스트 라이브러리에서 assertNotNull을 가져오기 위해 필요

fun getUserName(user: User?): String {
    // User 객체가 null이 아닐 것이라는 가정 하에 작업을 진행합니다.
    return assertNotNull(user) {
        // 만약 user가 null이라면, 이 블록은 실행되지 않고 오류를 발생시킵니다.
        throw IllegalArgumentException("User 객체는 null이 될 수 없습니다.")
    }.name
}

data class User(val name: String)

fun main() {
    val user = User("Alice")
    println(getUserName(user))  // 정상적으로 출력: Alice

    // 다음 줄은 오류를 발생시킵니다 (null인 경우를 테스트)
    // println(getUserName(null))  // 컴파일 오류 발생: User 객체는 null이 될 수 없습니다.
}
```

### 함수 반환값에 대한 assertNotNull 사용

```kotlin
import kotlin.test.*

fun fetchData(): String? {
    // 실제 로직에서 데이터를 가져오는 부분
    return "데이터 내용"
}

fun processData(data: String?) {
    // 데이터가 null이 아님을 확인하고 작업을 진행합니다.
    assertNotNull(data) {
        throw IllegalStateException("데이터는 null이 될 수 없습니다.")
    }
    println("처리된 데이터: ${data.toUpperCase()}")
}

fun main() {
    val data = fetchData()
    processData(data)  // 정상적으로 출력: 처리된 데이터: DATA 내용

    // 다음 줄은 오류를 발생시킵니다 (null인 경우를 테스트)
    // processData(null)  // 컴파일 오류 발생: 데이터는 null이 될 수 없습니다.
}
```

## 간단한 팁

- `NonNullAssertions`는 주로 테스트 코드나 중요한 비즈니스 로직에서 사용됩니다.
- 실제 애플리케이션에서는 `null` 안전성을 최대한 고려하여 함수와 변수를 설계하는 것이 좋습니다. 예를 들어, nullable 타입을 사용할 때는 명확한 이유와 처리 로직을 함께 명시하세요.

이렇게 `NonNullAssertions`를 이해하고 사용하면 코드의 안정성을 크게 높일 수 있어요. 궁금한 점이 있으면 언제든지 물어보세요! 함께 성장해 나가요. 😊