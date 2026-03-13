# 84. Property Delegation (속성 위임)

안녕하세요! 코틀린 프로그래밍을 처음 접하는 분들을 위해 이번 챕터에서는 **속성 위임(Property Delegation)**에 대해 쉽게 설명해 드릴게요. 이 개념은 코틀린에서 속성(변수)를 더 유연하게 관리할 수 있게 해주는 멋진 기능이에요. 간단하게 말해서, 기본 속성을 다른 클래스나 객체로 위임해서 복잡한 로직을 처리할 수 있게 하는 거죠. 이제 차근차근 이해해 보도록 할게요!

## 기본 개념

### 속성 위임이란?
코틀린에서 속성 위임은 기본 속성(`val` 또는 `var`)이 실제로 값을 가지는 것이 아니라 다른 객체의 메소드를 통해 값을 가져오거나 설정하도록 위임하는 방식입니다. 이렇게 하면 속성에 복잡한 로직을 추가하거나 다른 객체의 데이터를 사용할 수 있어요.

### `by` 키워드 사용하기
속성 위임을 구현할 때는 `by` 키워드를 사용합니다. 코드는 다음과 같이 작성됩니다:

```kotlin
val/var propertyName by delegateObject
```

여기서 `delegateObject`는 위임을 처리할 클래스나 객체입니다.

## 읽기 전용 속성 위임 (`val`)

### 예제 코드: `BasicRead.kt`

```kotlin
// 패키지 선언
package propertydelegation

import atomictest.eq // 테스트를 위한 라이브러리
import kotlin.reflect.KProperty // 리플렉션 관련 클래스

// 위임을 처리할 클래스
class Readable(val i: Int) {
    // 속성 `value`를 `BasicRead` 객체에 위임
    val value: String by BasicRead()
}

// 위임을 처리하는 객체
class BasicRead {
    // getValue 메소드 정의
    operator fun getValue(
        r: Readable, 
        property: KProperty<*> // 속성에 대한 메타데이터
    ): String {
        return "getValue: ${r.i}" // Readable 객체의 `i` 값을 반환
    }
}

// 메인 함수 예시
fun main() {
    val x = Readable(11) // Readable 객체 생성
    val y = Readable(17) // 또 다른 Readable 객체 생성
    
    // 값 비교 테스트
    println(x.value) // "getValue: 11" 출력
    println(y.value) // "getValue: 17" 출력
}
```

**핵심 포인트:**
- `Readable` 클래스의 `value` 속성은 `BasicRead` 객체에 위임됩니다.
- `BasicRead` 클래스는 `getValue()` 메소드를 통해 `Readable` 객체의 `i` 값을 가져와서 문자열로 변환합니다.
- `getValue()` 메소드는 `KProperty` 타입의 두 번째 매개변수를 받아서 속성에 대한 메타데이터를 받습니다.

## 읽기/쓰기 속성 위임 (`var`)

### 예제 코드: `BasicReadWrite.kt`

```kotlin
// 패키지 선언
package propertydelegation

import atomictest.eq // 테스트를 위한 라이브러리
import kotlin.reflect.KProperty // 리플렉션 관련 클래스

// 위임을 처리할 클래스
class ReadWriteable(var i: Int) {
    var msg: String = "" // 추가적인 메시지 변수
    var value: String by BasicReadWrite() // 속성 위임
}

// 위임을 처리하는 객체
class BasicReadWrite {
    // getValue 메소드 정의
    operator fun getValue(
        rw: ReadWriteable, 
        property: KProperty<*>
    ): String {
        return "getValue: ${rw.i}" // ReadWriteable 객체의 `i` 값을 반환
    }
    
    // setValue 메소드 정의
    operator fun setValue(
        rw: ReadWriteable, 
        property: KProperty<*>, 
        value: String
    ) {
        rw.i = value.toIntOrNull() ?: 0 // 문자열을 정수로 변환, 변환 실패 시 0으로 설정
        rw.msg = "setValue to ${rw.i}" // 설정 메시지 저장
    }
}

// 메인 함수 예시
fun main() {
    val x = ReadWriteable(11) // 객체 생성
    println(x.value) // "getValue: 11" 출력
    x.value = "99" // 값 설정
    println(x.msg) // "setValue to 99" 출력
    println(x.value) // "getValue: 99" 출력
}
```

**핵심 포인트:**
- `ReadWriteable` 클래스의 `value` 속성은 `BasicReadWrite` 객체에 위임됩니다.
- `BasicReadWrite` 클래스는 `getValue()`와 `setValue()` 메소드를 통해 읽기와 쓰기 동작을 처리합니다.
- `setValue()` 메소드는 설정된 값을 정수로 변환하고, 변환 실패 시 기본값(0)을 사용합니다.

## 인터페이스를 활용한 위임

### 예제 코드: `BasicRead2.kt` 및 `BasicReadWrite2.kt` ( 미완성 부분 포함 )

```kotlin
// 패키지 선언
package propertydelegation

import atomictest.eq // 테스트를 위한 라이브러리
import kotlin.properties.ReadOnlyProperty // 인터페이스 사용
import kotlin.reflect.KProperty // 리플렉션 관련 클래스

// 읽기 전용 위임 클래스
class Readable2(val i: Int) {
    val value: String by BasicRead2() // 인터페이스를 활용한 위임
    // SAM 변환을 이용한 더 간결한 방법
    val value2: String by ReadOnlyProperty { _, _ -> "getValue: $i" }
}

// 읽기 전용 인터페이스 구현 클래스
class BasicRead2 : ReadOnlyProperty<Readable2, String> {
    override operator fun getValue(
        thisRef: Readable2, 
        property: KProperty<*>
    ): String {
        return "getValue: ${thisRef.i}" // 값 반환
    }
}

// 읽기/쓰기 위임 클래스 예시 (완성되지 않은 부분)
class ReadWriteable2(var i: Int) {
    var msg: String = ""
    var value: String by BasicReadWrite2() // 인터페이스를 활용한 위임 예시
}

// 읽기/쓰기 인터페이스 구현 클래스 예시 (완성되지 않은 부분)
class BasicReadWrite2 : ReadWriteProperty<ReadWriteable2, String> {
    // getValue, setValue 메소드 구현 필요
}

// 메인 함수 예시
fun main() {
    val x = Readable2(11)
    val y = Readable2(17)
    println(x.value) // "getValue: 11" 출력
    println(x.value2) // "getValue: 11" 출력
    println(y.value) // "getValue: 17" 출력
    println(y.value2) // "getValue: 17" 출력
}
```

**핵심 포인트:**
- 인터페이스를 사용하면 위임 클래스를 명확하게 정의하고 코드의 가독성을 높일 수 있어요.
- `ReadOnlyProperty` 인터페이스를 사용하면 읽기 전용 속성 위임을 간결하게 구현할 수 있습니다.
- `ReadWriteProperty` 인터페이스를 사용하면 읽기/쓰기 속성 위임을 구현할 수 있습니다.

### 요약
- **속성 위임**은 복잡한 로직을 속성에 쉽게 통합할 수 있게 해줍니다.
- `by` 키워드를 사용하여 속성을 다른 객체에 위임합니다.
- 읽기 전용 속성은 `getValue()`만 필요하고, 읽기/쓰기 속성은 `getValue()`와 `setValue()`가 필요합니다.
- 인터페이스를 활용하면 코드의 명확성과 유지보수성을 높일 수 있습니다.

이제 코틀린 속성 위임에 대해 좀 더 익숙해졌기를 바라요! 궁금한 점이 있으면 언제든지 물어보세요!