# 30. 확장 함수 (Extension Functions)

안녕하세요! 코틀린 프로그래밍 초보자 여러분, 오늘은 확장 함수(Extension Functions)에 대해 배워볼게요. 쉽게 말해, 이미 있는 클래스에 새로운 기능을 추가하는 방법이에요. 마치 필요한 도구 하나만 추가하면 완벽해질 것 같은 라이브러리를 갖고 있는 상황에서, 직접 코드를 수정하지 않고도 편리하게 사용할 수 있게 도와주는 기능이죠.

## 기본 개념

### 확장 함수란?
확장 함수는 기존 클래스에 새로운 멤버 함수를 추가하는 방법입니다. 이때 확장 함수를 적용할 클래스를 **수신자(Receiver)**라고 부르는데요, 함수 정의 시에 수신자 타입을 앞에 붙여 주세요. 예를 들어:

```kotlin
fun String.singleQuote() = "'$this'"  // String 클래스에 새로운 함수 추가
fun String.doubleQuote() = "\"$this\"" // 또 다른 함수 추가
```

이렇게 정의하면 `String` 클래스에 `singleQuote()`와 `doubleQuote()`라는 새로운 메소드가 추가되는 거죠.

### 사용 방법
확장 함수는 마치 원래 클래스의 멤버 함수처럼 호출할 수 있어요. 다른 패키지에서 정의된 확장 함수를 사용하려면 해당 패키지를 import 해줘야 합니다. 예를 들어:

```kotlin
// 다른 패키지에서 정의된 확장 함수 사용
package other

import atomictest.eq
import extensionfunctions.doubleQuote  // 확장 함수 import
import extensionfunctions.singleQuote

fun main() {
    "Single".singleQuote() eq "'Single'"  // 확장 함수 호출
    "Double".doubleQuote() eq "\"Double\"" // 확장 함수 호출
}
```

### `this` 키워드
확장 함수에서 `this` 키워드는 수신자 객체를 가리키는데요, 일반 클래스 내에서처럼 생략할 수도 있어요. 예를 들어:

```kotlin
// 여러 번의 인용 처리 확장 함수
package extensionfunctions

import atomictest.eq

fun String.strangeQuote() = this.singleQuote().singleQuote()  // 첫 번째 this는 암묵적으로 이해됨
fun String.tooManyQuotes() = doubleQuote().doubleQuote()  // 두 번째 호출 시 this 생략 가능

fun main() {
    "Hi".strangeQuote() eq "''Hi''"  // 결과 확인
    "Hi".tooManyQuotes() eq "\"\"Hi\"\""  // 결과 확인
}
```

### 제한 사항
확장 함수는 확장하는 클래스의 **공개된 멤버**에만 접근할 수 있어요. 즉, 확장 함수는 기존 함수와 동일한 동작만 수행할 수 있습니다. 예를 들어, `Book` 클래스에 확장 함수를 추가할 때:

```kotlin
// Book 클래스에 확장 함수 추가
package extensionfunctions

import atomictest.eq

class Book(val title: String)

fun Book.categorize(category: String) = """title: "$title", category: $category"""

fun main() {
    val book = Book("Dracula")
    book.categorize("Vampire") eq """title: "Dracula", category: Vampire"""  // 확장 함수 호출
}
```

`this`를 생략하고도 코드가 더 간결해지죠? 이렇게 확장 함수는 코드를 더 읽기 쉽게 만들어줍니다.

## 핵심 요약
- **확장 함수**는 기존 클래스에 새로운 기능을 추가하는 방법입니다.
- 함수 정의 시 수신자 타입을 앞에 붙여 `fun ReceiverType.함수명() { ... }` 형태로 작성합니다.
- 호출 시 마치 원래 클래스의 멤버 함수처럼 사용할 수 있어요.
- `this` 키워드는 수신자 객체를 가리키며 생략 가능합니다.
- 확장 함수는 확장 대상 클래스의 공개 멤버만 접근 가능합니다.

이제 확장 함수를 활용해 코드를 더 간결하고 읽기 쉽게 만들어 보세요! 궁금한 점이 있으면 언제든지 물어보세요. 함께 배워가요!

### 연습 문제
- **연습**: 자신의 클래스에 확장 함수를 추가해보세요. 예를 들어, `Person` 클래스에 나이를 포맷팅하는 함수를 추가해보세요.
- **해답**: [www.AtomicKotlin.com](http://www.AtomicKotlin.com) 에서 제공되는 연습 문제와 해답을 확인해보세요!