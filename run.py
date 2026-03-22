"""
Facebook Group Product Posting Automation
Main execution file with modular structure
"""
import warnings
from time import sleep

from facebook_bot import FacebookBot
from products import PRODUCTS, FACEBOOK_GROUPS

warnings.filterwarnings("ignore")


class ProductPoster:
    """Product posting manager"""
    
    def __init__(self):
        self.bot = FacebookBot()
        self.total_posts = 0
        self.successful_posts = 0
        self.failed_posts = 0
        self.failed_groups = []  # Track failed group IDs with error details
    
    def start(self):
        """Start bot and login"""
        self.bot.start_browser()
        self.bot.login()
        sleep(4)
    
    def post_all_products(self):
        """Post all products to all groups"""
        print(f"\n{'='*60}")
        print(f"📦 {len(PRODUCTS)} products to be posted in {len(FACEBOOK_GROUPS)} groups")
        print(f"{'='*60}\n")
        
        for product_index, product in enumerate(PRODUCTS, 1):
            product_name = product["name"]
            
            # Support both "image" (single) and "images" (multiple)
            if "images" in product:
                images = product["images"]  # List of images
            elif "image" in product:
                images = [product["image"]]  # Single image as list
            else:
                print(f"❌ No images found for {product_name}, skipping...")
                continue
            
            description = product["description"]
            
            print(f"\n{'='*60}")
            print(f"🛍️  [{product_index}/{len(PRODUCTS)}] {product_name}")
            print(f"   📸 Images: {len(images)}")
            print(f"{'='*60}")
            
            # Generate AI text ONCE per product (not per group)
            try:
                generated_text = self.bot.ai_generator.generate_post_text(description)
                if not generated_text or len(generated_text) < 20:
                    generated_text = description
                print(f"✅ Text ready: {len(generated_text)} chars")
            except Exception as e:
                print(f"⚠️ AI failed: {str(e)[:60]}")
                generated_text = description
            
            # Post to all groups with the same text and images
            self._post_product_to_groups(product_name, images, generated_text, description)
            
            print(f"\n✅ {product_name} posted to all groups!\n")
        
        self._print_summary()
    
    def _post_product_to_groups(self, product_name, images, text_to_post, description):
        """Post single product to all groups with pre-generated text and images"""
        for group_index, group_id in enumerate(FACEBOOK_GROUPS, 1):
            try:
                print(f"  [{group_index}/{len(FACEBOOK_GROUPS)}] Group: {group_id}")
                
                self.bot.navigate_to_group(group_id)
                # Pass images, text, product name, and price (extracted from description)
                self.bot.create_post(images, text_to_post, product_name, description)
                self.bot.publish_post()
                
                self.successful_posts += 1
                self.total_posts += 1
                print(f"  ✅ Success!")
                
            except Exception as e:
                self.failed_posts += 1
                self.total_posts += 1
                error_msg = str(e)[:80]
                print(f"  ❌ Error: {error_msg}")
                
                # Record failed group with details
                self.failed_groups.append({
                    'product': product_name,
                    'group_id': group_id,
                    'error': error_msg
                })
                continue
    
    def _print_summary(self):
        """Print summary statistics and save failed groups to file"""
        print(f"\n{'='*60}")
        print("📊 SUMMARY")
        print(f"{'='*60}")
        print(f"Total posting attempts: {self.total_posts}")
        print(f"✅ Successful: {self.successful_posts}")
        print(f"❌ Failed: {self.failed_posts}")
        print(f"📈 Success rate: {(self.successful_posts/self.total_posts*100):.1f}%")
        print(f"{'='*60}\n")
        
        # Save failed groups to file
        if self.failed_groups:
            try:
                with open('failed.txt', 'w', encoding='utf-8') as f:
                    f.write("FAILED GROUP IDs\n")
                    f.write("=" * 60 + "\n\n")
                    
                    # Extract unique group IDs from failed attempts
                    failed_ids = list(set([failed['group_id'] for failed in self.failed_groups]))
                    failed_ids.sort()  # Sort for readability
                    
                    for group_id in failed_ids:
                        f.write(f"{group_id}\n")
                    
                    f.write("\n" + "=" * 60 + "\n")
                    f.write(f"Total failed groups: {len(failed_ids)}\n")
                
                print(f"📄 Failed group IDs saved to: failed.txt")
            except Exception as e:
                print(f"⚠️ Could not save failed.txt: {e}")
        else:
            print("🎉 No failed posts!")
    
    def stop(self):
        """Stop bot"""
        self.bot.close()


def main():
    """Main function"""
    print("\n🚀 Starting Facebook Product Posting Bot...\n")
    
    poster = ProductPoster()
    
    try:
        poster.start()
        poster.post_all_products()
    except KeyboardInterrupt:
        print("\n\n⚠️ Stopped by user")
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
    finally:
        poster.stop()
        print("\n👋 Program terminated\n")


if __name__ == "__main__":
    main()