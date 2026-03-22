# AI Text Generator Module
from config import get_ai_client, AI_MODEL

class AITextGenerator:
    """AI class for generating Facebook post texts"""
    
    def __init__(self):
        self.client = get_ai_client()
        print("🤖 AI client ready")
    
    def generate_post_text(self, product_description):
        """
        Generate unique post text from product description
        
        Args:
            product_description (str): Product description
            
        Returns:
            str: AI-generated post text
        """
        try:
            prompt = (
                f"Maak een korte, aantrekkelijke Facebook post (maximaal 200 woorden) "
                f"voor dit tweedehands artikel: {product_description}. "
                f"Wees enthousiast en gebruik emoji's. "
                f"BELANGRIJK: "
                f"- Gebruik GEEN hashtags (#). "
                f"- Gebruik GEEN Markdown formatting zoals **bold**, *italic*, of __underline__. "
                f"- Schrijf alleen gewone tekst met emoji's. "
                f"- Gebruik geen sterretjes (*) of andere formatteringstekens."
            )
            
            response = self.client.chat.completions.create(
                model=AI_MODEL,
                messages=[{"role": "user", "content": prompt}],
            )
            
            generated_text = response.choices[0].message.content
            
            # Clean up any Markdown formatting that might have slipped through
            if generated_text:
                # Remove ** for bold
                generated_text = generated_text.replace('**', '')
                # Remove __ for bold/underline
                generated_text = generated_text.replace('__', '')
                # Remove single * for italic (but keep if it's part of normal text)
                # Only remove if it appears in pairs like *text*
                import re
                generated_text = re.sub(r'\*([^\*]+)\*', r'\1', generated_text)
            
            if generated_text and len(generated_text) > 30:
                return generated_text
            else:
                return product_description
            
        except Exception as e:
            print(f"⚠️ AI generation failed: {str(e)[:60]}")
            return product_description
    
    def generate_custom_text(self, prompt):
        """
        Generate text with custom prompt
        
        Args:
            prompt (str): Prompt to send to AI
            
        Returns:
            str: AI-generated text
        """
        try:
            response = self.client.chat.completions.create(
                model=AI_MODEL,
                messages=[{"role": "user", "content": prompt}],
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            print(f"⚠️ AI text generation failed: {e}")
            return ""
