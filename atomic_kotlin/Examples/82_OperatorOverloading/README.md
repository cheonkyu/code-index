# 82. 연산자 오버로딩 (Operator Overloading)

안녕하세요! 코틀린 프로그래밍을 처음 접하시는 분들을 위해 연산자 오버로딩에 대해 쉽게 설명해 드릴게요. 연산자 오버로딩이란 이미 있는 연산자에 새로운 의미를 더하는 것과 같아요. 쉽게 말해, `+` 같은 연산자가 새롭게 만든 데이터 타입이나 기존 데이터 타입에 대해 원하는 방식으로 동작하도록 만드는 거죠.

## 기본 개념

### 연산자 오버로딩의 필요성
- **기존 언어의 경험**: C++에서는 연산자 오버로딩이 가능했지만, 가비지 컬렉션이 없어서 복잡했어요. Java는 이를 거부했지만, Python과 Scala는 이를 시도했어요. Kotlin은 이들 언어의 교훈을 배워 연산자 오버로딩을 간소화하면서도 익숙하고 합리적인 범위로 제한했어요.
- **간결성**: 가비지 컬렉션 덕분에 Kotlin에서는 연산자 오버로딩을 좀 더 쉽게 만들 수 있게 되었어요. 하지만 연산자의 우선 순위는 바꿀 수 없어요.

### 연산자 오버로딩 예시: `Num` 클래스

```kotlin
// 연산자 오버로딩 예시: Num 클래스
package operatoroverloading

import atomictest.eq

// 기본 데이터 클래스 정의
data class Num(val n: Int)

// 연산자 오버로딩을 위한 확장 함수 정의 (+ 연산자 오버로딩)
operator fun Num.plus(rval: Num): Num {
    return Num(n + rval.n)
}

fun main() {
    // 연산자 오버로딩 사용 예시
    val num1 = Num(4)
    val num2 = Num(5)
    val result = num1 + num2 // Num(9) 반환
    result eq Num(9) // 결과 확인

    // 직접 함수 호출 방식으로도 가능
    val result2 = num1.plus(num2) // 동일한 결과
    result2 eq Num(9) // 결과 확인
}
```

**설명**:
- `operator fun` 키워드를 사용해 연산자 오버로딩을 정의합니다. 여기서는 `+` 연산자를 오버로딩하고 있어요.
- `Num` 클래스의 인스턴스 간 덧셈 연산을 정의하였고, 이를 통해 더 직관적인 코드를 작성할 수 있어요.

### 멤버 함수 연산자 오버로딩

```kotlin
// 멤버 함수로 연산자 오버로딩 예시: Num2 클래스
package operatoroverloading

import atomictest.eq

data class Num2(private val n: Int) {
    // 멤버 함수로 연산자 오버로딩
    operator fun plus(rval: Num2): Num2 {
        return Num2(n + rval.n)
    }
}

fun main() {
    // 멤버 함수 연산자 오버로딩 사용 예시
    val num3 = Num2(4)
    val num4 = Num2(5)
    val result3 = num3 + num4 // Num2(9) 반환
    result3 eq Num2(9) // 결과 확인

    // 주의: private 멤버에 접근 불가
    // operator fun Num2.minus(rval: Num2): Num2 = { Num2(n - rval.n) } // 컴파일 오류 가능
}
```

**설명**:
- 멤버 함수로 연산자 오버로딩을 정의할 수 있어요. 이때 클래스 내부의 private 멤버에 접근하는 것이 가능해요. 하지만 예시에서처럼 private 멤버에 대한 접근은 제한적일 수 있어요.

### 연산자 오버로딩의 실제 활용 예시: `Molecule` 클래스

```kotlin
// 분자 모델 예시: Molecule 클래스
package operatoroverloading

import atomictest.eq

data class Molecule(
    val id: Int = Companion.nextId,
    var attached: Molecule? = null
) {
    companion object {
        private var nextId = 0 // ID 생성기
    }

    // 연산자 오버로딩: `+` 연산자를 사용해 분자 연결
    operator fun plus(other: Molecule): Unit {
        attached = other
    }
}

fun main() {
    val molecule1 = Molecule()
    val molecule2 = Molecule()
    molecule1 + molecule2 // 분자 연결

    // 출력 예시
    molecule1 eq "Molecule(id=0, attached=$molecule2)" // 실제 출력은 조금 다를 수 있음
}
```

**설명**:
- `+` 연산자를 통해 `Molecule` 객체 간 연결을 표현할 수 있어요. 이렇게 하면 코드가 더 직관적이고 의미 있게 보일 수 있어요.
- 하지만 주의할 점은 순환 참조로 인한 스택 오버플로우 문제가 발생할 수 있으니 주의해야 해요. 예를 들어 `molecule2 + molecule1`을 호출하고 `molecule2`를 출력하면 문제가 생길 수 있어요.

### 동등성 (Equality) 연산자 이해

코틀린에서는 `==`와 `!=` 연산자를 통해 객체의 동등성을 확인할 수 있어요.

```kotlin
// 동등성 이해 예시
package operatoroverloading

import atomictest.eq

// 기본 클래스 예시
class A(val i: Int)

// 데이터 클래스 예시
data class D(val i: Int)

fun main() {
    // 일반 클래스
    val a = A(1)
    val b = A(1)
    val c = a
    println(a == b) // false: 다른 객체 참조
    println(a == c) // true: 동일 객체 참조

    // 데이터 클래스
    val d = D(1)
    val e = D(1)
    println(d == e) // true: 동일한 데이터 값 비교
}
```

**설명**:
- **일반 클래스**: 객체 참조 비교로 동작하므로 `a == b`는 `false`가 될 수 있어요.
- **데이터 클래스**: 내부 데이터만 비교하므로 `d == e`는 `true`가 될 수 있어요.

### 핵심 요약
- **연산자 오버로딩**은 이미 있는 연산자에 새로운 의미를 부여하여 코드를 더 직관적으로 만드는 기법이에요.
- **Kotlin**에서는 연산자 오버로딩을 간단하게 정의할 수 있지만, 연산자 우선 순위는 변경할 수 없어요.
- **동등성 연산자**는 클래스 타입에 따라 참조 비교와 데이터 비교를 다르게 적용해요.

이제 연산자 오버로딩에 대해 좀 더 익숙해졌기를 바라요! 궁금한 점이 있으면 언제든지 물어봐 주세요!