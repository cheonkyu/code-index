# 38. SafeCallsAndElvis

안녕하세요, 코틀린 초보자 여러분! 오늘은 코틀린에서 안전하게 객체 메소드 호출을 다루는 방법에 대해 배워볼게요. 특히, `SafeCalls`와 `Elvis 연산자`에 대해 알아보면서 코드 안전성과 가독성을 향상시키는 방법을 배워볼게요.

## 안전한 호출 (SafeCalls)

`SafeCalls`는 불확실한 객체 참조가 있을 때 메소드 호출을 안전하게 처리하는 방법입니다. 만약 객체가 `null`이라면 메소드 호출은 아무 일도 일어나지 않아요. 이렇게 하면 `NullPointerException`을 피할 수 있어요.

### 예제 코드

```kotlin
fun main() {
    var maybeObject: String? = null
    
    // 안전 호출 사용 예시
    val safeResult = maybeObject?.length // 만약 maybeObject가 null이면 length는 0으로 처리됩니다.
    println("길이: $safeResult") // 출력: 길이: 0

    // 문자열이 있는 경우
    maybeObject = "안녕하세요"
    val lengthResult = maybeObject?.length // 정상적으로 길이 계산
    println("길이: $lengthResult") // 출력: 길이: 13
}
```

### 설명
- `maybeObject?.length`: 만약 `maybeObject`가 `null`이면 호출이 무시되고 값이 자동으로 `0`으로 처리됩니다.
- 이렇게 하면 `null` 참조로 인한 오류를 걱정할 필요 없이 안전하게 코드를 작성할 수 있어요.

## Elvis 연산자

`Elvis 연산자` (`?.`)는 `SafeCalls`와 비슷하지만, 좀 더 간결하게 코드를 작성할 수 있게 해주는 연산자예요. 주로 변수가 `null`일 때 메소드 호출을 하기 전에 안전하게 체크하는 데 사용됩니다. Elvis 연산자는 결과가 `null`일 경우 기본값을 반환하거나 다음 표현식으로 넘어가게 할 수 있어요.

### 예제 코드

```kotlin
fun main() {
    var optionalValue: String? = null
    
    // Elvis 연산자 사용 예시
    val defaultMessage = optionalValue ?: "기본 메시지" // optionalValue가 null이면 "기본 메시지"가 사용됨
    println("메시지: $defaultMessage") // 출력: 메시지: 기본 메시지

    // 문자열이 있는 경우
    optionalValue = "코틀린 초보자"
    val formattedMessage = optionalValue ?: "%s님, 환영합니다!" // 문자열이 있으므로 포맷 문자열이 사용됨
    println("형식 메시지: $formattedMessage") // 출력: 형식 메시지: 코틀린 초보자님, 환영합니다!
}
```

### 설명
- `optionalValue ?: "기본 메시지"`: `optionalValue`가 `null`이면 `"기본 메시지"`를 반환합니다.
- Elvis 연산자는 코드의 가독성을 높이면서 동시에 안전한 코딩을 도와줍니다.

## 핵심 요약

- **SafeCalls**: 객체가 `null`일 때 메소드 호출을 안전하게 처리하여 `NullPointerException`을 방지합니다.
- **Elvis 연산자**: 간결하게 `SafeCalls`를 구현하며, `null`일 때 기본값을 반환하거나 다음 표현식으로 넘어가는 기능을 제공합니다.

이렇게 하면 코틀린 코드에서 객체 참조의 안전성을 확보하면서도 깔끔하고 유지보수하기 쉬운 코드를 작성할 수 있어요. 연습을 통해 이 개념들을 익혀보세요! 질문이 있으면 언제든지 물어보세요!