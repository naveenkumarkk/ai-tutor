window.onload = async function() {
    const answerContainers = document.querySelectorAll('.answer_container');
    
    // Check if there are any answer containers on the page
    if (answerContainers.length > 0) {
      // Get the last answer container
      const lastAnswerContainer = answerContainers[answerContainers.length - 1];
      
      // Scroll the last answer container into view smoothly
      lastAnswerContainer.scrollIntoView({ behavior: 'smooth' });
    }
    //scrollToBottom();
}