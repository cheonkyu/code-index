# 47. MemberReferences

안녕하세요! 이번 챕터에서는 Kotlin에서 **멤버 참조(Member References)**에 대해 배워볼게요. 멤버 참조는 클래스의 함수, 속성, 생성자를 간결하게 호출하거나 참조할 수 있는 편리한 방법이에요. 특히 초보자분들껜 조금 헷갈릴 수 있지만, 차근차근 따라 해보면 어렵지 않아요!

## 핵심 개념 요약

1. **멤버 참조란?**
   - 클래스 내의 함수, 속성, 생성자를 호출하거나 참조하는 방법입니다.
   - 이중 콜론 `::`을 사용해 클래스 이름과 멤버 이름을 구분해요.

2. **사용 사례**
   - **속성 참조**: 간단한 람다 대신 속성을 직접 참조할 수 있어요.
   - **함수 참조**: 복잡한 조건을 함수로 정의하고 이를 참조할 수 있어요.
   - **생성자 참조**: 생성자 자체를 참조하는 것도 가능하지만, 이 부분은 이번 챕터에서는 다루지 않을게요.

## 속성 참조 예제

### 코드 예제: `PropertyReference.kt`

```kotlin
package memberreferences1
import atomictest.eq

data class Message(
    val sender: String,          // 발신자
    val text: String,            // 메시지 내용
    val isRead: Boolean          // 읽혔는지 여부
)

fun main() {
    // 메시지 목록 생성
    val messages = listOf(
        Message("Kitty", "Hey!", true),   // 읽혔음
        Message("Kitty", "Where are you?", false)  // 읽지 않음
    )

    // 읽지 않은 메시지만 필터링
    val unread = messages.filterNot { Message::isRead }  // 메시지::isRead로 간단하게 처리 가능
    
    // 결과 확인
    unread.size eq 1  // 결과 크기가 1인지 확인
    unread.single().text eq "Where are you?"  // 첫 번째 메시지 내용이 "Where are you?"인지 확인
}
```

**설명:**
- `Message::isRead`로 읽혔는지 여부를 간단히 참조해요.
- 람다로 작성할 수도 있지만, 멤버 참조는 코드를 더 간결하게 만들어줍니다.

## 정렬 예제

### 코드 예제: `SortWith.kt`

```kotlin
package memberreferences1
import atomictest.eq
import kotlin.comparisons.*

fun main() {
    val messages = listOf(
        Message("Kitty", "Hey!", true),   // 읽혔음
        Message("Kitty", "Where are you?", false),  // 읽지 않음
        Message("Boss", "Meeting today", false)   // 읽지 않음
    )

    // 메시지 정렬: 먼저 읽지 않은 메시지로 정렬하고, 그 다음 발신자 이름으로 정렬
    val sortedMessages = messages.sortedWith(compareBy(Message::isRead, Message::sender))
    
    // 정렬 결과 확인
    sortedMessages eq listOf(
        Message("Boss", "Meeting today", false),  // 첫 번째: 읽지 않은 메시지, 발신자 이름으로 정렬
        Message("Kitty", "Where are you?", false), // 두 번째: 읽지 않은 메시지, 발신자 이름으로 정렬
        Message("Kitty", "Hey!", true)            // 세 번째: 읽은 메시지, 발신자 이름으로 정렬
    )
}
```

**설명:**
- `compareBy` 함수를 사용해 속성을 기준으로 정렬할 때 멤버 참조를 활용해요.
- `Message::isRead`와 `Message::sender`를 통해 정렬 기준을 쉽게 지정할 수 있어요.

## 함수 참조 예제

### 코드 예제: `FunctionReference.kt`

```kotlin
package memberreferences2
import atomictest.eq

data class Message(
    val sender: String,          // 발신자
    val text: String,            // 메시지 내용
    val isRead: Boolean,         // 읽혔는지 여부
    val attachments: List<Attachment>  // 첨부 파일 리스트
)

data class Attachment(
    val type: String,            // 첨부 파일 타입
    val name: String             // 첨부 파일 이름
)

// 메시지가 중요한지 판별하는 함수
fun Message.isImportant(): Boolean {
    return text.contains("Salary increase") ||  // 텍스트에 "급여 인상" 포함 여부
           attachments.any { it.type == "image" && it.name.contains("cat") }  // 첨부 파일 중 이미지 타입이고 "cat" 포함 여부
}

fun main() {
    // 중요 메시지 체크
    val messages = listOf(
        Message("Boss", "Let's discuss goals for next year", false, listOf(Attachment("image", "cute cats")))
    )
    
    // 중요 메시지가 있는지 확인
    messages.any { it.isImportant() } eq true  // 중요 메시지가 있는지 확인
}
```

**설명:**
- 복잡한 조건을 별도의 함수 `isImportant()`로 정의하고 이를 멤버 참조로 사용해요.
- 이렇게 하면 코드가 더 명확해지고 유지보수가 용이해져요.

## 최상위 함수 참조 예제

### 코드 예제: `TopLevelFunctionRef.kt`

```kotlin
package memberreferences2
import atomictest.eq

fun ignore(message: Message) {
    !message.isImportant() &&  // 중요 메시지가 아니면
    message.sender in setOf("Boss", "Mom")  // 발신자가 "Boss" 또는 "Mom"인 경우
}

fun main() {
    val text = "Let's discuss goals for the next year"
    val msgs = listOf(
        Message("Boss", text, false, listOf()),
        Message("Boss", text, false, listOf(Attachment("image", "cute cats")))
    )

    // 특정 조건에 맞는 메시지 필터링
    msgs.filter(::ignore).size eq 1  // ignore 함수로 필터링한 결과 크기 확인
    msgs.filterNot(::ignore).size eq 1  // ignore 함수와 반대 조건으로 필터링
}
```

**설명:**
- `ignore`라는 최상위 함수를 `::ignore`로 참조해요.
- 클래스 멤버가 아닌 일반 함수도 참조할 수 있어요.

---

이렇게 멤버 참조를 활용하면 코드가 더 간결하고 이해하기 쉬워집니다. 연습을 통해 익숙해지면 Kotlin 프로그래밍에서 큰 도움이 될 거예요! 궁금한 점이 있으면 언제든지 물어보세요! 😊