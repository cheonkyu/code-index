# 51. Sequences

안녕하세요, 초보자 분들께 코틀린의 `Sequence` 개념을 친절하게 설명해 드릴게요! 이 주제는 처음 접하실 때 조금 어렵게 느껴질 수 있지만, 차근차근 따라가다 보면 쉽게 이해하실 수 있을 거예요.

## 기본 개념 이해하기

### Sequence란 무엇인가요?
코틀린의 `Sequence`는 `List`와 비슷해 보이지만, 몇 가지 중요한 차이점이 있어요:
- **인덱싱 불가능**: `Sequence`에서는 특정 위치에 있는 요소를 바로 접근할 수 없어요. 오직 순차적으로 순회해야 해요.
- **효율적인 연쇄 작업**: 이런 제한 덕분에 연속적인 작업을 매우 효율적으로 처리할 수 있어요. 마치 스트림처럼요! Kotlin에서는 이 개념을 `Sequence`로 구현하면서 Java 8의 `Stream`과 호환성을 유지하기 위해 이 이름을 선택했어요.

### Eager Evaluation vs Lazy Evaluation
#### Eager Evaluation (즉시 계산)
- **작동 방식**: 코틀린의 기본 리스트 연산은 즉시 계산해요. 예를 들어, `filter()`, `map()`, `any()` 등을 연속적으로 적용하면 각 단계에서 모든 요소를 처리해요.
  ```kotlin
  fun main() {
      val list = listOf(1, 2, 3, 4)
      list.filter { it % 2 == 0 }  // 짝수만 필터링
          .map { it * it }         // 각 요소를 제곱
          .any { it < 10 }        // 결과 중 10보다 작은 것이 있는지 확인
          .let { println(it) }    // 결과 출력
  }
  ```
  **예시 코드 설명**:
  - `list.filter { it % 2 == 0 }`: 짝수만 남김 (결과: `[2, 4]`)
  - `.map { it * it }`: 각 요소를 제곱 (결과: `[4, 16]`)
  - `.any { it < 10 }`: 결과 중 10보다 작은 것이 있는지 확인 (결과: `true`)

  하지만 이 방법은 모든 요소를 순차적으로 처리하므로 긴 리스트에서는 비효율적일 수 있어요.

#### Lazy Evaluation (지연 계산)
- **작동 방식**: 필요할 때만 계산해요. 이 방식은 특히 큰 데이터셋에서 효율적이죠. `asSequence()` 함수를 사용하면 `List`를 `Sequence`로 변환하여 지연 계산을 적용할 수 있어요.
  ```kotlin
  package sequences

  import atomictest.*

  // 보조 함수 정의
  fun Int.isEven(): Boolean {
      trace("$this.isEven()")
      return this % 2 == 0
  }

  fun Int.square(): Int {
      trace("$this.square()")
      return this * this
  }

  fun Int.lessThanTen(): Boolean {
      trace("$this.lessThanTen()")
      return this < 10
  }

  fun main() {
      val list = listOf(1, 2, 3, 4)
      
      trace(">>> List (즉시 계산):")
      trace(
          list
              .filter(Int::isEven)
              .map(Int::square)
              .any(Int::lessThanTen)
      )
      
      trace(">>> Sequence (지연 계산):")
      trace(
          list.asSequence()
              .filter(Int::isEven)
              .map(Int::square)
              .any(Int::lessThanTen)
      )
  }
  ```
  **예시 코드 설명**:
  - `List`에서는 모든 짝수를 필터링하고 제곱한 후 결과를 확인하지만,
  - `Sequence`에서는 실제로 필요할 때만 각 단계를 처리해요. 예를 들어, `any()`가 `true`를 반환하면 그 순간까지만 계산이 진행되고 그 후에는 멈추죠.

  **출력 예시**:
  ```
  >>> List (즉시 계산):
  1.isEven()
  2.isEven()
  3.isEven()
  4.isEven()
  2.square()
  4.square()
  4.lessThanTen()
  true
  
  >>> Sequence (지연 계산):
  1.isEven()
  2.isEven()
  2.square()
  4.lessThanTen()
  true
  ```

### 핵심 요약
- **Sequence**는 순차적으로 처리되며, 인덱싱이 불가능해요.
- **Lazy Evaluation**을 통해 필요한 순간에만 연산을 수행하여 효율성을 크게 향상시킬 수 있어요.
- `asSequence()` 함수를 사용하면 `List`에서도 지연 계산의 이점을 누릴 수 있어요.

이렇게 이해하셨다면, `Sequence`를 활용해 효율적인 데이터 처리를 시도해 보세요! 궁금한 점이 있으면 언제든지 물어보세요. 😉