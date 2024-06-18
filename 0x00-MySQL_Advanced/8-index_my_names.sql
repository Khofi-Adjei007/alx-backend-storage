USE holberton;

-- Drop the index if it exists to ensure idempotency
DROP INDEX IF EXISTS idx_name_first ON names;

-- Create the index on the first letter of the name column
CREATE INDEX idx_name_first ON names (LEFT(name, 1));