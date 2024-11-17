def text(Question):
  json_format = """
  {
    response: [
      {
        type: "text",
        content: "..."
      },
      {
        type: "code",
        language: "example: javascript, python, sql, etc",
        content: "..."
      }
    ]
  }
  """

  return f"""
  The question is: {Question}

  Show the response as json in the folowing format: {json_format}

  Follow these rules for the response:
  - for any paragraph, create an object with type "text" and content as the paragraph
  - for any code, create an object with type "code" and content as the code
  - don't show anything in markdown format
  - don't the main response in markdown format
  - dont use ** or `` in the response
  - for libs and frameworks, use the main language of the code, ex: for svelte use javascript, for ruby on rails use ruby, for react use javascript, for laravel use php, etc
  - for question involving javascript frameworks, use html as programming language
  """
