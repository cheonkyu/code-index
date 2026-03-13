# 37. NullableTypes

안녕하세요! Kotlin 초보자 분들을 위해 `NullableTypes` 주제에 대해 쉽게 설명해 드릴게요. 이 주제는 함수가 때때로 값을 반환하지 못할 때 어떻게 처리하는지에 대해 배워보겠습니다. 특히, `null` 값이 어떻게 사용되는지와 이를 어떻게 안전하게 다루는지에 대해 알아볼 거예요.

## 왜 `null` 값이 중요할까요?

상상해보세요, 지도에서 특정 키가 있는 값을 찾아볼 때가 있어요. 만약 그 키가 존재하지 않으면, 어떤 언어에서는 그 결과가 `null`이 됩니다. 즉, "값이 없음"을 의미하죠. Kotlin에서는 이를 간단하게 `null`로 표현해요. 하지만 `null`을 의미 있는 값과 동일하게 다루면 큰 문제가 생길 수 있어요. 예를 들어, Java에서는 `null`을 참조하려고 하면 `NullPointerException`이 발생할 수 있어요. 이렇게 되면 프로그램이 갑자기 멈추거나 심각한 오류를 일으킬 수 있어요.

### Kotlin의 해결책: `nullable` 타입

Kotlin은 이런 문제를 해결하기 위해 `nullable` 타입을 도입했어요. 기본적으로 타입은 `non-nullable`로 설정되지만, 특정 경우에는 `null` 값을 허용할 수 있도록 타입을 명시적으로 지정할 수 있어요. 이렇게 하면 컴파일러가 오류를 미리 잡아낼 수 있어요.

### 핵심 개념 요약

1. **기본 타입은 `non-nullable`**:
   - 기본적으로 모든 변수는 `null`을 가질 수 없어요. 예를 들어, `String` 타입의 변수는 항상 문자열을 가져야 합니다.
   ```kotlin
   val s1: String = "abc"  // 기본적으로 non-nullable 타입
   ```

2. **`nullable` 타입 지정**:
   - `null` 값을 허용하려면 타입 뒤에 `?`를 붙여주세요.
   ```kotlin
   val s3: String? = null  // null 값을 가질 수 있는 타입
   val s4: String? = "abc" // null 또는 문자열을 가질 수 있음
   ```

3. **타입 일치**:
   - `non-nullable` 타입 변수에는 `null`을 할당할 수 없어요.
   ```kotlin
   // 오류: Type mismatch: inferred type is String? but String was expected
   val s5: String = s4  // 오류 발생
   ```
   - 하지만 `nullable` 타입 변수에는 `null`을 할당할 수 있어요.
   ```kotlin
   val s6: String? = s4  // null 또는 문자열을 가질 수 있음
   ```

4. **`Map`에서의 `null`**:
   - Kotlin의 `Map`은 Java 기반이므로, 키에 해당하는 값이 없을 때 `null`을 반환합니다.
   ```kotlin
   val map = mapOf(0 to "yes", 1 to "no")
   val first: String? = map[0]  // 키가 존재하면 문자열 반환, 아니면 null 반환
   val second: String? = map[2] // 키가 존재하지 않으면 null 반환
   ```

### 예제 코드 설명

#### 기본 타입 예시
```kotlin
// 기본 타입은 non-nullable
val s1: String = "abc"  // 올바른 할당

// 오류: null을 할당할 수 없음
// val s2: String = null  // 컴파일 오류: Type mismatch: inferred type is String? but String was expected
```

#### nullable 타입 예시
```kotlin
// null을 포함할 수 있는 타입 지정
val s3: String? = null  // null 값 허용
val s4: String? = "abc" // null 또는 문자열 가능

// 타입 일치 오류 예시
// val s5: String = s4  // 오류: Type mismatch
val s6: String? = s4    // null 또는 문자열 가능

// 출력 확인
s1 == "abc"          // true
s3 == null          // true
s4 == "abc"         // true
s6 == "abc"         // true
```

#### `Map`에서의 `null` 처리
```kotlin
val map = mapOf(0 to "yes", 1 to "no")
val first: String? = map[0]  // 키가 있으면 문자열, 없으면 null
val second: String? = map[2] // 키가 없으면 null 반환

println(first)  // "yes"
println(second) // null
```

### 중요한 사항
- **Null 체크**: `null` 값을 다룰 때는 항상 값이 존재하는지 확인하는 것이 중요해요. Kotlin에서는 `?:` 연산자(NPE 방지 연산자)나 `safe call` 연산자(`?.`)를 사용해 안전하게 다룰 수 있어요.
- **예외 처리**: Java와 마찬가지로 Kotlin에서도 `null` 참조 시 예외 처리를 잘 해야 합니다.

이렇게 `nullable` 타입을 이해하고 적절히 사용하면 Kotlin에서 안전하고 효율적인 코드를 작성할 수 있어요. 궁금한 점이 있으면 언제든지 물어보세요!