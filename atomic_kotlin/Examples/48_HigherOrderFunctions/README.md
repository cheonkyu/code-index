# 48. HigherOrderFunctions

안녕하세요! 오늘은 Atomic Kotlin에서 다루는 **HigherOrderFunctions**에 대해 초보자도 이해하기 쉽게 설명해 드릴게요. 고등 함수라는 이름에서 짐작하실 수 있듯이, 이 개념은 조금 더 복잡해 보이지만 걱정하지 마세요! 하나씩 천천히 알아보도록 하겠습니다.

## 핵심 개념 요약

### 1. **함수는 인자로 함수를 받을 수 있다**
   - **HigherOrderFunction**은 다른 함수를 인자로 받거나 반환하는 함수를 말합니다. 쉽게 말해, 함수도 물건처럼 다른 함수를 주고 받을 수 있다는 거죠!

### 2. **함수를 인자로 넘기기**
   - 예를 들어, 리스트의 요소를 처리할 때 특정 동작을 정의한 함수를 인자로 전달하여 유연하게 사용할 수 있습니다. 이렇게 하면 코드가 더 간결하고 재사용성이 높아집니다.

### 3. **함수의 반환값으로 함수 사용하기**
   - 고등 함수는 함수 자체를 반환할 수도 있어요. 이렇게 하면 다양한 동작을 동적으로 생성하고 적용할 수 있습니다.

## 예제 코드 설명

### 함수를 인자로 넘기는 예시

아래 코드는 `printMessage`라는 함수가 `messageFormatter`라는 함수를 인자로 받아 사용하는 예시입니다.

```kotlin
// 메시지 포맷팅 함수들 정의
fun capitalize(s: String): String {
    return s.toUpperCase()
}

fun underline(s: String): String {
    return s + "\n_____________"
}

// 메시지 출력 함수
fun printMessage(formatter: (String) -> String, message: String) {
    val formattedMessage = formatter(message)
    println(formattedMessage)
}

fun main() {
    // 함수를 인자로 전달하여 메시지 포맷팅
    printMessage({ capitalize("안녕하세요") }, "기본 메시지")
    printMessage({ underline("반갑습니다") }, "언더라인 메시지")
}
```

**설명:**
- `capitalize`와 `underline` 함수는 문자열을 특정 방식으로 포맷팅하는 함수들입니다.
- `printMessage` 함수는 `formatter`라는 이름의 함수를 인자로 받아서 이를 사용해 `message`를 포맷팅하고 출력합니다.
- `main` 함수에서는 `printMessage` 함수에 `capitalize`와 `underline` 함수를 인자로 전달하여 다양한 포맷팅 방식을 적용하고 출력합니다.

### 함수를 반환하는 예시

다음은 함수를 반환하는 예시입니다. 여기서는 사용자 입력에 따라 다른 동작을 수행하는 함수를 생성합니다.

```kotlin
// 사용자 입력에 따른 동작 정의
fun createOperation(operationType: String): (Int) -> Int {
    return when (operationType) {
        "덧셈" -> { x: Int -> x + 1 }
        "뺄셈" -> { x: Int -> x - 1 }
        else -> { x: Int -> x } // 기본 동작
    }
}

fun main() {
    // 함수 반환 예시
    val addOperation = createOperation("덧셈")
    val subtractOperation = createOperation("뺄셈")

    println(addOperation(5))   // 출력: 6
    println(subtractOperation(5)) // 출력: 4
}
```

**설명:**
- `createOperation` 함수는 문자열 인자 `operationType`에 따라 덧셈 또는 뺄셈 함수를 반환합니다.
- `main` 함수에서는 이 함수를 사용해 동적으로 다른 연산 함수를 생성하고 사용합니다.

## 요약

고등 함수는 코드를 더 유연하고 재사용 가능하게 만드는 강력한 도구입니다. 함수를 인자로 받거나 반환함으로써 다양한 상황에 맞게 동작을 정의하고 적용할 수 있습니다. 이런 개념을 익히면 Kotlin 프로그래밍에서 훨씬 더 창의적이고 효율적인 코드를 작성할 수 있을 거예요!

궁금한 점이 있으면 언제든지 물어보세요! 함께 배우면서 성장해 나가요! 😊