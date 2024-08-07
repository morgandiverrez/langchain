"""Test OpenLLM wrapper."""

from langchain_community.llms.openllm import OpenLLM


def test_openllm_llm_local() -> None:
    llm = OpenLLM(model_name="flan-t5", model_id="google/flan-t5-small")
    output = llm.invoke("Say foo:")
    assert isinstance(output, str)


def test_openllm_with_kwargs() -> None:
    llm = OpenLLM(
        model_name="flan-t5", model_id="google/flan-t5-small", temperature=0.84
    )
    output = llm.invoke("Say bar:")
    assert isinstance(output, str)
