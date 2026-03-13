# 23. 예외 처리 (Exceptions)

안녕하세요, 코틀린 프로그래밍을 처음 접하시는 여러분! 이번 챕터에서는 **예외 처리**에 대해 배워볼게요. 예외 처리는 프로그램이 예상치 못한 상황에 마주쳤을 때 어떻게 대응할지 알려주는 중요한 개념이에요. 쉽게 말해, 일상에서 누군가와 대화 중에 이해가 안 되는 부분이 생겼을 때 잠시 멈추고 다시 설명을 요청하는 것과 비슷해요.

## 예외란 무엇인가요?

예외란 "이 부분에 동의하지 않습니다"라는 뜻의 표현처럼, 프로그램이 정상적인 흐름을 유지할 수 없는 **특별한 상황**을 의미해요. 예를 들어, 어떤 작업을 수행하다가 더 이상 진행이 불가능한 상황이 생겼을 때, 그 순간을 중단하고 문제를 해결할 수 있는 다른 부분으로 넘기는 거죠. 이렇게 하면 프로그램 전체가 멈추지 않고 더 안전하게 동작할 수 있어요.

### 예외 발생 예시: `toInt()` 함수

코틀린에서 문자열을 정수로 변환하는 `toInt()` 함수를 생각해볼게요. 만약 숫자가 아닌 문자열을 이 함수에 넣으면 어떻게 될까요?

```kotlin
package exceptions

// 주석을 해제하면 예외가 발생합니다.
// fun erroneousCode() {
//     val i = "1$".toInt()  // 숫자가 아닌 문자열로 예외 발생
// }

fun erroneousCode() {
    // 예시로 예외를 발생시키지 않도록 주석 처리했습니다.
    // 실제 예외 상황을 테스트하려면 위 주석을 해제하세요.
}

fun main() {
    erroneousCode()
}
```

**예외 발생 시 상황:**
- 주석을 해제하면 `"1$".toInt()` 호출 시 `NumberFormatException`이 발생합니다.
- 이 예외는 프로그램 실행 중에 문제가 발생했다는 신호를 보내요.
- 출력 예시:
  ```
  Exception in thread "main" java.lang.NumberFormatException: For input string: "1$"
     at java.lang.NumberFormatException.forInputString(NumberFormatException.java:65)
     at java.lang.Integer.parseInt(Integer.java:580)
     at java.lang.Integer.parseInt(Integer.java:615)
     at ToIntExceptionKt.erroneousCode(ToIntException.kt:6)
     at ToIntExceptionKt.main(ToIntException.kt:10)
  ```

### 스택 트레이스 이해하기

위의 스택 트레이스는 오류 발생 위치를 정확히 알려줍니다. 파일 이름과 줄 번호를 통해 어디서 문제가 생겼는지 쉽게 파악할 수 있어요.

```
파일: ToIntException.kt  줄: 6  -> `toInt()` 호출 위치
파일: ToIntException.kt  줄: 10  -> `erroneousCode()` 호출 위치
```

### 예외 처리 방법: `capture()` 함수 사용

예외를 직접 확인하면서 테스트하는 건 조금 번거로울 수 있어요. 그래서 `AtomicTest` 패키지의 `capture()` 함수를 활용해요. 이 함수는 예외가 발생했을 때 그 내용을 쉽게 비교할 수 있게 해줍니다.

```kotlin
import atomictest.*

fun main() {
    capture {
        "1$".toInt()  // 예외 발생 예상
    } eq "NumberFormatException: For input string: \"1$\""
}
```

### 예외 대신 null 반환하기

예외 대신 `null`을 사용하는 방법도 있어요. `null`은 "값이 없음"을 의미하는 특별한 상수예요. 예를 들어, 문자열을 정수로 변환할 때 변환이 불가능하면 `null`을 반환할 수 있어요.

```kotlin
import atomictest.eq

fun main() {
    "1$".toIntOrNull() eq null  // 변환 불가능 시 null 반환 확인
}
```

### 요약

- **예외**는 프로그램이 정상적으로 진행될 수 없는 상황을 의미해요.
- **예외 발생** 시 프로그램은 그 지점에서 중단되고, 문제를 다른 부분으로 넘깁니다.
- **스택 트레이스**는 오류 발생 위치를 정확히 알려줘요.
- **`capture()`** 함수는 예외 테스트를 쉽게 만들어줘요.
- **`null` 반환**은 예외 없이 실패를 표현하는 방법이에요.

이제 코틀린에서 예외 처리에 대해 조금 더 자신감 있게 다룰 수 있을 거예요! 연습을 통해 더 익숙해지세요. 다음 챕터에서는 더 다양한 예외 처리 기법을 배워볼게요. 응원합니다! 😊