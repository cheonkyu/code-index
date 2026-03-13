# 28. PropertyAccessors

안녕하세요, 코틀린 프로그래밍을 처음 배우는 여러분! 오늘은 Kotlin에서 **Property Accessors**에 대해 배워볼게요. 쉽게 말해, 프로퍼티를 읽고 쓰는 방법에 대해 알아보는 거예요. 이해하기 쉽게 단계별로 설명해드릴게요.

## 기본 프로퍼티 읽기와 쓰기

### 기본 개념
Kotlin에서 기본적인 프로퍼티를 읽거나 쓸 때는 간단한 방법으로 처리해요. 프로퍼티 이름만으로 값을 읽거나 쓸 수 있어요.

```kotlin
// 예제: 기본 프로퍼티 읽기와 쓰기
package propertyaccessors

import atomictest.eq

class Data(var i: Int)  // 변수형 프로퍼티 'i' 생성

fun main() {
    val data = Data(10)  // 'Data' 객체 생성하고 'i' 프로퍼티 초기값 10으로 설정
    data.i eq 10         // 프로퍼티 'i' 읽기 (값 확인)
    data.i = 20          // 프로퍼티 'i'에 새로운 값 20 할당
}
```

- **읽기 (Getter)**: 프로퍼티 이름을 사용해 값을 읽어옵니다. 예를 들어, `data.i`로 값을 확인할 수 있어요.
- **쓰기 (Setter)**: 할당 연산자 `=`를 사용해 값을 설정합니다. 예를 들어, `data.i = 20`으로 값을 변경할 수 있어요.

### 커스텀 프로퍼티 접근자 (Getter와 Setter)

기본적으로는 이렇게 동작하지만, 때로는 프로퍼티의 읽기와 쓰기 동작을 커스텀하고 싶을 수 있어요. 이때 **Getter**와 **Setter**를 직접 정의할 수 있어요.

#### Getter (값 읽기) 정의하기
Getter는 프로퍼티 값을 읽어올 때 사용되는 함수예요. 프로퍼티 바로 아래에 `get()`을 정의하면 돼요.

```kotlin
// 예제: 기본 Getter와 Setter 구현
package propertyaccessors

import atomictest.*

class Default {
    var i: Int = 0  // 기본 프로퍼티 'i' 정의

    // Getter 정의
    get() {
        trace("get()")  // 읽기 동작 기록
        return field  // 실제 프로퍼티 값 반환
    }

    // Setter 정의
    set(value) {
        trace("set($value)")  // 쓰기 동작 기록
        field = value  // 프로퍼티 값 변경
    }
}

fun main() {
    val d = Default()
    d.i = 2  // Setter 사용해 값 설정
    trace(d.i)  // Getter 사용해 값 확인
    trace eq """
        set(2)  // 쓰기 동작 확인
        get()   // 읽기 동작 확인
        2       // 최종 값 확인
        """
}
```

#### Setter (값 쓰기) 정의하기
Setter는 프로퍼티 값을 쓸 때 사용되는 함수예요. `set()`을 바로 아래에 정의하면 돼요.

```kotlin
// 예제: Getter와 Setter로 동작 기록
package propertyaccessors

import atomictest.*

class LogChanges {
    var n: Int = 0  // 기본 프로퍼티 'n' 정의

    // Setter 정의 (쓰기 동작 기록 포함)
    set(value) {
        trace("$field becomes $value")  // 변경 전/후 값 기록
        field = value  // 프로퍼티 값 변경
    }
}

fun main() {
    val lc = LogChanges()
    lc.n eq 0  // 초기 값 확인
    lc.n = 2   // Setter로 값 변경

    lc.n eq 2  // 변경된 값 확인
    trace eq "0 becomes 2"  // 동작 기록 확인
}
```

### Getter와 Setter의 순서 무관
Getter와 Setter의 정의 순서는 중요하지 않아요. 필요에 따라 하나만 정의해도 돼요.

```kotlin
// 예제: Getter만 정의한 경우
package propertyaccessors

import atomictest.*

class PartialAccessor {
    var message: String = "Initial"

    // Getter만 정의
    get() {
        trace("Getting message: ${field}")
        return field
    }
}

fun main() {
    val pa = PartialAccessor()
    trace(pa.message)  // Getter 동작 확인
}
```

### 접근 제한
프로퍼티나 그 접근자를 `private`로 설정하면 외부에서 접근을 제한할 수 있어요. 예를 들어, 변경은 내부에서만 허용할 수 있어요.

```kotlin
// 예제: 접근 제한
package propertyaccessors

import atomictest.eq

class Counter {
    var value: Int = 0  // 기본 프로퍼티 'value' 정의

    // Setter만 private으로 설정
    private set

    fun inc() = value++  // 내부에서만 증가 가능
}

fun main() {
    val counter = Counter()
    repeat(10) {
        counter.inc()  // 내부에서만 증가
    }
    counter.value eq 10  // 외부에서 값 확인 가능 (읽기만 가능)
}
```

### 계산형 프로퍼티
필드 없이 계산형 프로퍼티를 만들 수도 있어요. 이런 프로퍼티는 각 호출 시마다 계산되어 결과를 반환해요.

```kotlin
// 예제: 계산형 프로퍼티
package propertyaccessors

import atomictest.eq

class Cage(private val maxCapacity: Int) {
    private val hamsters = mutableListOf<Hamster>()

    // 계산형 프로퍼티 'capacity' 정의
    val capacity: Int
    get() = maxCapacity - hamsters.size

    // 계산형 프로퍼티 'full' 정의
    val full: Boolean
    get() = hamsters.size == maxCapacity

    fun put(hamster: Hamster): Boolean {
        if (full) return false
        hamsters += hamster
        return true
    }

    fun take(): Hamster {
        return hamsters.removeAt(0)
    }
}

fun main() {
    val cage = Cage(2)
    cage.full eq false  // 초기 상태 확인
    cage.capacity eq 2  // 초기 용량 확인

    cage.put(Hamster("Alice")) eq true  // 햄스터 추가 성공 확인
    cage.put(Hamster("Bob")) eq true   // 추가 성공 확인
    cage.full eq true                  // 햄스터가 가득 찬 상태 확인
    cage.capacity eq 0                 // 현재 용량 확인
    cage.take()                        // 햄스터 제거 후 용량 확인
    cage.capacity eq 1                 // 제거 후 용량 확인
}
```

### 핵심 요약
1. **Getter**: 프로퍼티 값을 읽어오는 함수 (`get()`)
2. **Setter**: 프로퍼티 값을 설정하는 함수 (`set(value)`)
3. **커스텀 접근자**: 프로퍼티 동작을 커스텀할 수 있어요 (예: 동작 기록).
4. **접근 제한**: `private`로 설정하면 외부 접근 제한 가능.
5. **계산형 프로퍼티**: 필드 없이 값을 계산해서 반환하는 프로퍼티 생성 가능.

이렇게 코틀린의 프로퍼티 접근자에 대해 간단히 알아봤어요. 실습을 통해 더 많이 연습해보면 이해도가 훨씬 높아질 거예요! 궁금한 점이 있으면 언제든지 물어봐주세요. 😊