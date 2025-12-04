response.content[0], len(response.content)
messages = []
messages.append(dict(role="user", content=msg))
messages.append(dict(role=response.role, content=response.content))
contents = []
contents.append(dict(type="tool_result", tool_use_id=response.id, content=response.content[0].input['s']))
messages.append(dict(role="user", content=contents))
def create_test_message(stop_reason):
    return anthropic.types.Message(
        id='test_id',
        content=[],
        model='claude-haiku-4-5',
        role='assistant',
        type='message',
        usage=anthropic.types.Usage(input_tokens=0, output_tokens=0),
        stop_reason=stop_reason
    )