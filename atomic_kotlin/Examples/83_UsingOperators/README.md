# 83. 연산자 오버로딩 이해하기: 초보자를 위한 가이드

안녕하세요! 오늘은 코틀린 프로그래밍에서 중요한 개념 중 하나인 **연산자 오버로딩**에 대해 배워볼게요. 처음에는 조금 어려울 수 있지만, 몇 가지 예제와 함께 차근차근 이해해 나가면 어렵지 않아요!

## 연산자 오버로딩이란 무엇인가요?

연산자 오버로딩이란 기본적으로 **기존 연산자의 동작을 자신의 클래스나 타입에서 다르게 정의하는 것**을 말해요. 코틀린에서는 주로 라이브러리를 만들 때 사용되지만, 일상적으로는 표준 라이브러리에 이미 많은 연산자 오버로딩이 내장되어 있어요. 이를 통해 코드가 더 직관적이고 편리해지죠.

### 자주 사용되는 연산자 오버로딩 예제

#### 리스트 예제: `get()`, `set()`, `contains()`

코틀린 표준 라이브러리에서는 리스트와 같은 컬렉션을 다룰 때 유용한 연산자 오버로딩을 제공해요. 예를 들어, `MutableList`를 사용할 때 다음과 같이 간결하게 코드를 작성할 수 있어요:

```kotlin
import atomictest.eq  // 테스트 라이브러리 가정

fun main() {
    val list = MutableList(10) { 'a' + it }.apply {  // 리스트 초기화
        // [ ]를 사용하여 요소 접근 (get 연산자 오버로딩)
        this[7] eq 'h'   // 'h'를 얻음
        // 명시적으로 get() 호출
        this.get(8) eq 'i'
        
        // [ ]를 사용하여 요소 수정 (set 연산자 오버로딩)
        this[9] = 'x'  // 리스트의 10번째 요소를 'x'로 설정
        // 명시적으로 set() 호출
        this.set(9, 'x')
        this[9] eq 'x'  // 변경 확인
        
        // 포함 여부 확인 (contains 연산자 오버로딩)
        ('d' in list) eq true  // 'd'가 리스트에 포함되어 있는지 확인
        // 명시적으로 contains() 호출
        this.contains('e') eq true
    }
}
```

**핵심 개념 요약:**
- `[ ]`를 사용하면 `get()`과 `set()` 연산자가 오버로딩되어 리스트 요소를 쉽게 접근 및 수정할 수 있어요.
- `in` 연산자는 `contains()` 연산자를 오버로딩한 결과예요.

#### `+=` 연산자와 `+` 연산자

`+=` 연산자는 컬렉션을 직접 수정하는 반면, `+` 연산자는 새로운 컬렉션을 생성해요:

```kotlin
import atomictest.eq  // 테스트 라이브러리 가정

fun main() {
    val mutableList = mutableListOf(1, 2, 3)
    
    // += 연산자: 기존 컬렉션 수정
    mutableList += 4  // 연산자 오버로딩: plusAssign() 호출
    mutableList eq "[1, 2, 3, 4]"  // 수정된 리스트 확인
    
    // + 연산자: 새로운 컬렉션 생성
    mutableList + 99 eq "[1, 2, 3, 4, 99]"  // 새로운 리스트 생성
    mutableList eq "[1, 2, 3, 4]"  // 원래 리스트는 그대로 유지
    
    val list = listOf(1)  // 읽기 전용 컬렉션
    val newList = list + 2  // 새로운 리스트 생성
    list eq "[1]"  // 원래 리스트는 변경되지 않음
    newList eq "[1, 2]"  // 새로운 리스트 확인
}

**핵심 개념 요약:**
- `+=`는 컬렉션을 직접 수정해요.
- `+`는 새로운 컬렉션을 생성해요. 읽기 전용 컬렉션에서는 `+=`가 작동하지 않아 `+` 연산자가 대신 사용되요.

#### `compareTo()` 메소드와 비교 연산자

`Comparable` 인터페이스를 구현하면 클래스의 인스턴스 간 비교가 가능해져요:

```kotlin
import atomictest.eq  // 테스트 라이브러리 가정

package usingoperators

data class Contact(val name: String, val mobile: String) : Comparable<Contact> {
    override fun compareTo(other: Contact): Int = name.compareTo(other.name)
}

fun main() {
    val alice = Contact("Alice", "0123456789")
    val bob = Contact("Bob", "9876543210")
    val carl = Contact("Carl", "5678901234")
    
    // 비교 연산자 사용
    (alice < bob) eq true  // 이름 순으로 비교
    (alice <= bob) eq true
    (alice > bob) eq false
    (alice >= bob) eq false
    
    val contacts = listOf(bob, carl, alice)
    contacts.sorted() eq listOf(alice, bob, carl)  // 정렬
    contacts.sortedDescending() eq listOf(carl, bob, alice)  // 내림차순 정렬
}

**핵심 개념 요약:**
- `Comparable` 인터페이스를 구현하고 `compareTo()` 메소드를 오버로딩하면 `<`, `>`, `<=`, `>=` 등의 비교 연산자를 사용할 수 있어요.
- 이는 컬렉션 정렬이나 범위 확인 등에 유용해요.

### 마무리

연산자 오버로딩은 코틀린에서 매우 강력하고 유용한 기능이에요. 표준 라이브러리와 함께 사용하면 코드가 훨씬 더 직관적이고 간결해집니다. 처음에는 다소 복잡하게 느껴질 수 있지만, 예제를 통해 조금씩 이해해 나가면 훨씬 쉬워질 거예요!

궁금한 점이 있으면 언제든지 물어보세요! 함께 배워나가요!