import asyncio
from django.shortcuts import render

# Define your coroutine
async def my_async_function(param):
    await asyncio.sleep(2)  # Simulate an I/O-bound task
    return {"message": f"Processed {param}"}

# View function
async def index(request):
    # Example parameter, you can get it from request if needed
    param = 'example_param'
    
    # Run the async function
    result = await my_async_function(param)
    
    # Pass the result to your template context if needed
    context = {
        'async_result': result,
    }
    
    return render(request, 'pyscript/index.html', context)
