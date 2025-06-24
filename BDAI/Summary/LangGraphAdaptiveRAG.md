# LangGraph Adaptive RAG
## Agent로 하면 되지 않나?
- Agent로 하면 자체적으로 판단 하에 진행하는 건 좋지만, Agent가 너무 많아지면 controllability가 떨어짐(내가 원하는 방향성과 다를 수 있음)
- 정형화하기 위해 with_structured_output()에 쿼리를 넣는 것
```py
# LLM 초기화 및 함수 호출을 통한 구조화된 출력 생성
llm = ChatOpenAI(model=MODEL_NAME, temperature=0)
structured_llm_router = llm.with_structured_output(RouteQuery)
```

## Hallucination VS Relevant
- Hallucination: 정보에 없는 정보를 바탕으로 만들어낸 답변
- Relevant: 질문과 관련성이 있는 답변인가?