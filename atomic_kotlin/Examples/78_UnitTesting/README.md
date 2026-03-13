# 78. UnitTesting: 코틀린 프로그래밍의 기본 단위 테스트 이해하기

안녕하세요! 코틀린 프로그래밍을 배우고 계신 여러분, 이번 챕터에서는 **단위 테스트**에 대해 쉽게 알아보도록 하겠습니다. 단위 테스트는 함수나 코드 조각의 정확성을 확인하기 위해 작성하는 테스트입니다. 쉽게 말해, 코드의 작은 부분들을 따로 따로 체크해서 오류나 문제점을 빨리 찾아내는 역할을 해요. 이렇게 하면 개발 속도가 훨씬 빨라집니다!

## 기본 개념 이해하기

### 단위 테스트란?

- **단위**라는 말은 코드의 작은 부분, 주로 함수 하나를 의미합니다. 이 작은 조각이 잘 작동하는지 독립적으로 테스트한다는 뜻이에요.
- **예시**: 만약 `calculateDiscount()`라는 함수가 있다면, 이 함수만 따로 떼어 놓고 다양한 입력에 대해 올바르게 동작하는지 확인하는 거죠.

### 왜 중요한가요?

- **오류 빠른 발견**: 코드에 문제가 생겼을 때 빨리 알려주므로 수정도 빠르게 할 수 있어요.
- **신뢰성 향상**: 테스트를 통해 코드의 안정성을 높일 수 있어요.

### 주요 도구들

- **kotlin.test**: 코틀린의 표준 라이브러리에 포함된 테스트 프레임워크입니다. 다양한 테스트 라이브러리를 쉽게 사용할 수 있게 도와줘요.
  - **추가 의존성**: 프로젝트의 `build.gradle` 파일에 다음 줄을 추가해주세요.
    ```gradle
    testImplementation "org.jetbrains.kotlin:kotlin-test-common"
    ```

## 기본 테스트 함수들

kotlin.test는 여러 유용한 함수를 제공해요:

- **assertEquals**: 예상 값과 실제 값을 비교합니다.
  ```kotlin
  assertEquals(expectedValue, actualValue, "오류 메시지")
  ```
  **예시**:
  ```kotlin
  fun fortyTwo() = 42

  fun testFortyTwo() {
      assertEquals(42, fortyTwo(), "값이 틀어짐")
  }
  ```

- **assertTrue**: 불리언 표현식의 참/거짓을 확인합니다.
  ```kotlin
  assertTrue(condition, "오류 메시지")
  ```
  **예시**:
  ```kot린
  fun allGood(b: Boolean = true) = b

  fun testAllGood() {
      assertTrue(allGood(true), "조건이 만족되지 않음")
  }
  ```

## 코드 예제 살펴보기

### `expect()` 함수 사용법

`expect()` 함수는 코드 블록의 결과와 예상 값을 쉽게 비교할 수 있게 도와줘요:
```kotlin
// UnitTesting/UsingExpect.kt
package unittesting

import kotlin.test.*

fun testFortyTwo2(n: Int = 42) {
    expect(n, "값이 틀림", { fortyTwo() })
}

fun main() {
    testFortyTwo2()
    // 실패 시 출력 예시
    assertFails { testFortyTwo2(43) } // "expected: <43> but was: <42>"
}
```

### 주요 포인트 요약

- **단위 테스트**는 작은 코드 조각을 따로 체크하여 오류를 빠르게 찾아냅니다.
- **kotlin.test** 라이브러리는 테스트를 쉽게 작성할 수 있게 도와줍니다.
- **assertEquals**와 **assertTrue** 같은 함수들은 예상 결과와 실제 결과를 비교합니다.
- **expect()** 함수는 코드 블록의 결과를 쉽게 테스트할 수 있게 해줍니다.

이제 여러분도 간단한 단위 테스트를 작성해보고 코드의 정확성을 확인해보세요! 궁금한 점이 있으면 언제든지 물어봐주세요. 함께 배워가는 재미를 느껴보세요!