from src.app import query_llm, UserDetail
import asyncio
import pytest

pytest_plugins = ('pytest_asyncio',)

@pytest.mark.asyncio
async def test_query_llm_function_returns_correct_information():
    result = await query_llm(
        """{"query":"This has nothing to do with anything
but there is a man named Harvey, and he just turned 40."}"""
    )

    assert isinstance(result, UserDetail)
    assert result.name == "Harvey"
    assert result.age == 40